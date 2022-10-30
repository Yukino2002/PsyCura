from calendar import month
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from .decorators import allowed_users
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .Google import Create_Service, convert_to_RFC_datetime






@login_required(login_url='sign_in')
@allowed_users(allowed_users=['patient'])
def p_home(request):
    patient = Patient.objects.get(user=request.user)
    return render(request, 'Users/patient/profile/profile.html', {'patient':patient})







@login_required(login_url='sign_in')
@allowed_users(allowed_users=['patient'])
def p_appoint(request, d_id):
        patient = Patient.objects.get(user=request.user)
        doctor = Doctor.objects.get(pk=d_id)

        if request.method == 'POST':
            date = request.POST.get('date')
            time = request.POST.get('time')
            year, month, day, hour, minute = int(date[0:4]), int(date[5:7]), int(date[8:10]), int(time[0:2]), int(time[3:5])
            
            CLIENT_SECRET_FILE='static/assets/client_secret_PsyCura.json'
            API_NAME='calendar'
            API_VERSION='v3'
            SCOPES=['https://www.googleapis.com/auth/calendar']
            calendar_id = '5lnu2uakgegiudqs7taniti1bs@group.calendar.google.com'

            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
            event_request_body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(year, month, day, hour, minute),
                    'timeZone': 'Asia/Kolkata',
                },
                'end': {
                    'dateTime': convert_to_RFC_datetime(year, month, day, hour+1, minute),
                    'timeZone': 'Asia/Kolkata',
                },
                'summary': 'PsyCura Appointment',
                'description': 'Meeting',
                'colorId': 1,
                'attendees': [
                    {
                        'email': str(doctor.user.email),
                        'displayName': str(doctor.user.first_name) + ' ' + str(doctor.user.last_name),
                        'organizer': True,
                        'self': True,
                        'resource': False,
                        'optional': False,
                        'responseStatus': 'accepted',
                    },
                    {
                        'email': str(patient.user.email),
                        'displayName': str(patient.user.first_name) + ' ' + str(patient.user.last_name),
                        'organizer': False,
                        'self': False,
                        'resource': False,
                        'optional': False,
                        'responseStatus': 'accepted',
                    }
                ],
            }

            response = service.events().insert(calendarId=calendar_id, body=event_request_body).execute()
            return redirect('Users:p_home')

        return render(request, 'Users/patient/doctors/p_doctors_appoint.html', {'patient':patient, 'doctor':doctor})










@login_required(login_url='sign_in')
@allowed_users(allowed_users=['patient'])
def p_doctors(request):
    patient = Patient.objects.get(user=request.user)
    doctors = Doctor.objects.all().filter(is_approved='A')

    if request.method == "POST":
        specialization = request.POST.get("specialization")
        specialization = specialization.lower()
        specialization = specialization[0].upper() + specialization[1:]
        doctors = Doctor.objects.all().filter(is_approved='A', specialization=specialization)

    return render(request, "Users/patient/doctors/d_list.html", {'patient':patient, 'doctors':doctors})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['patient'])
def wallet(request):
    mssg=""
    patient = Patient.objects.get(pk=request.user.id)
    if request.method == "POST":
        action = request.POST.get("type")
        amount = int(request.POST.get("amount"))


        is_auth = authenticate(
            email = request.user.email,
            password = request.POST.get("passwd")
        )

        if is_auth is None:
            mssg = "Invalid Password"
        elif action == "add":
            patient.wallet_balance += amount
            mssg = "Money added to wallet"
        elif action == "withdraw":
            if patient.wallet_balance >= amount:
                patient.wallet_balance -= amount
                mssg = "Money withdrawn from wallet"
            else:
                mssg = "Invalid amount. Please check the current balance"
        patient.save()
    return render(request,"Users/patient/wallet.html", {"patient":patient,"mssg":mssg})

















@login_required(login_url='sign_in')
@allowed_users(allowed_users=['doctor'])
def d_home(request):
    doctor = Doctor.objects.get(pk = request.user.id)
    return render(request, 'Users/doctor/home.html', {'doctor':doctor})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['sponsor'])
def s_home(request):
    return render(request, 'Users/sponsor/home.html')























@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def home(request):
    return render(request, 'Users/staff/profile/profile.html', {'staff':request.user})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def doctors_pending(request):
    doctors = Doctor.objects.all().filter(is_approved='P')
    return render(request, 'Users/staff/doctors/d_list.html', {'staff':request.user, 'doctors':doctors})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def doctors_approved(request):
    doctors = Doctor.objects.all().filter(is_approved='A')
    return render(request, 'Users/staff/doctors/d_list.html', {'staff':request.user, 'doctors':doctors})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def doctors_banned(request):
    doctors = Doctor.objects.all().filter(is_approved='B')
    return render(request, 'Users/staff/doctors/d_list.html', {'staff':request.user, 'doctors':doctors})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def doctor_update(request, d_id):
    doctor = Doctor.objects.get(pk=d_id)

    if request.method == 'POST':
        doctor.is_approved = request.POST.get('is_approved')
        doctor.save()
        return redirect('Users:doctors_pending')

    return render(request, 'Users/staff/doctors/d_update.html', {'staff':request.user, 'doctor':doctor})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def sponsors_pending(request):
    sponsors = Sponsor.objects.all().filter(is_approved='P')
    return render(request, 'Users/staff/sponsors/s_list.html', {'staff':request.user, 'sponsors':sponsors})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def sponsors_approved(request):
    sponsors = Sponsor.objects.all().filter(is_approved='A')
    return render(request, 'Users/staff/sponsors/s_list.html', {'staff':request.user, 'sponsors':sponsors})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def sponsors_banned(request):
    sponsors = Sponsor.objects.all().filter(is_approved='B')
    return render(request, 'Users/staff/sponsors/s_list.html', {'staff':request.user, 'sponsors':sponsors})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def sponsors_update(request, s_id):
    sponsor = Sponsor.objects.get(pk=s_id)

    if request.method == 'POST':
        sponsor.is_approved = request.POST.get('is_approved')
        sponsor.save()
        return redirect('Users:sponsors_pending')

    return render(request, 'Users/staff/sponsors/s_update.html', {'staff':request.user, 'sponsor':sponsor})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def forums(request):
    # forums = Forum.objects.all()
    return render(request, 'Users/staff/forums/forums.html', {'staff':request.user})


@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    return redirect('sign_in')