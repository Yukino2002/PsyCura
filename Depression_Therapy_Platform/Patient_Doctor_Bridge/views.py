from django.contrib.auth.decorators import login_required
from django.db.models import OrderBy
from django.shortcuts import HttpResponse, render,redirect
from .decorators import allowed_users
from Users.models import *
from Interactions.models import *
from .models import *
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Create your views here.
@login_required(login_url="sign_in")
@allowed_users(['patient','doctor'])
def appointments(request):
    if request.method == "POST":
        type = request.POST.get("type")
        if type == "cancel":
            id = request.POST.get("id")
            Appointment.objects.get(pk = int(id)).delete()
            return redirect("Patient_Doctor_Bridge:appointments")
        else:
            decision = request.POST.get("")

    group = request.user.groups.all()[0].name
    if group == 'patient':
        patient = Patient.objects.get(pk = request.user.id)
        appointments = Appointment.objects.all().filter(patient = patient)
        pending_appointments = appointments.filter(approved = False)
        booked_appointments = appointments.filter(completed = False,approved= True)
    print(booked_appointments)
    completed_appointments = appointments.filter(completed = True,approved = True)
    print(completed_appointments)
    if group == 'patient':
        return render(request,"Users/patient/appointments.html",{'booked_appointments':booked_appointments,'completed_appointments':completed_appointments})
    else:
        return render(request,"Users/doctor/appointments.html",{'booked_appointments':booked_appointments,'completed_appointments':completed_appointments})


@login_required(login_url="sign_in")
@allowed_users(['patient'])
def book_appointment(request):
    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time")
        patient = Patient.objects.get(pk=request.user.id)
        doctor = Doctor.objects.get(pk=int(request.POST.get("doctor")))
        if date != "":
            new_appointment = Appointment(date = date,time = time,patient = patient,doctor = doctor)
            new_appointment.save()
            slot = Time_Table.objects.all().filter(doctor=doctor,date=date,time=time)[0]
            slot.patient = patient
            slot.save()
            appointments = Appointment.objects.all()
            return render(request,"Users/patient/appointments.html",{'appointments':appointments})
    
    # doctor_schedule = Time_Table.objects.all().filter(doctor=doctor,patient=None).order_by('date')
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    if os.path.exists("static/assets/tokens.json"):
        creds = Credentials.from_authorized_user_file("static/assets/tokens.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "static/assets/client_secret.json", SCOPES)
            creds = flow.run_local_server()
        with open("static/assets/tokens.json", 'w') as token:
            token.write(creds.to_json())
    print(creds)
    try:
        service = build('calendar', 'v3', credentials=creds)
        now=datetime.datetime.now()
        weekly_schedule = service.events().list(calendarId="primary",
                                                timeMin=now,
                                                timeMax=now + datetime.timedelta(weeks=1)
                                                ).execute()
        doctor_schedule = weekly_schedule.get('items',[])
        print(type(doctor_schedule))
        return render(request,"Users/patient/book_appointment.html",{'doctor':doctor,'doctor_schedule':[]})
    except HttpError as error:
        print("Hey")
        print("An error has occured %s" % error)
        return render(request,"Users/patient/book_appointment.html",{'doctor':doctor, 'doctor_schedule':[]})

    

# @login_required(login_url='sign_in')
# @allowed_users(['doctor'])
# def setTimeTable(request):
    



    

    





    
