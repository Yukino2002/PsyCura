from cmath import log
import sys
sys.path.append('..')
from Users import models
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    return render(request, 'homepage/homepage.html')


def about(request):
    return render(request, 'homepage/about.html')


def contact(request):
    return render(request, 'homepage/contact.html')


@unauthenticated_user
def sign_in(request):
    if request.method == 'POST':
        user = authenticate(
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )

        if user is not None:
            if user.groups.exists():
                group = user.groups.all()[0].name

                if group == 'patient':
                    login(request, user)
                    return redirect('Users:p_home')

                elif group == 'doctor':
                    doctor = models.Doctor.objects.get(user=user)
                    if doctor.is_approved == 'A':
                        login(request, user)
                        return redirect('Users:d_home')
                    
                    return redirect('sign_in')

                elif group == 'sponsor':
                    sponsor = models.Sponsor.objects.get(user=user)
                    if sponsor.is_approved == 'A':
                        login(request, user)
                        return redirect('Users:s_home')
                    
                    return redirect('sign_in')

            elif user.is_superuser:
                login(request, user)
                return redirect('Users:home')
            
        else:
            return render(request, 'authentication/sign_in.html')

    return render(request, 'authentication/sign_in.html')


@unauthenticated_user
def sign_up(request):
    return render(request, 'authentication/sign_up.html')


def create_user(request, group):
    user = get_user_model().objects.create_user(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        age=request.POST.get('age'),
        email=request.POST.get('email'),
        phone_number=request.POST.get('phone'),
        gender=request.POST.get('gender'),
        password=request.POST.get('password')
    )

    user.groups.add(group)

    return user


@unauthenticated_user
def p_sign_up(request):
    if request.method == 'POST':
        user = create_user(request, Group.objects.get(name='patient'))

        models.Patient.objects.create(
            user=user,
            past_diseases=request.POST.get('past_diseases'), 
            past_medication=request.POST.get('past_medication')
        )

        return redirect('sign_in')

    return render(request, 'authentication/forms/p_form.html')


@unauthenticated_user
def d_sign_up(request):
    if request.method == 'POST':
        user = create_user(request, Group.objects.get(name='doctor'))

        models.Doctor.objects.create(
            user=user,
            qualifications=request.POST.get('qualifications'), 
            certificate=request.POST.get('certficate')
        )

        return redirect('sign_in')

    return render(request, 'authentication/forms/d_form.html')


@unauthenticated_user
def s_sign_up(request):
    if request.method == 'POST':
        user = create_user(request, Group.objects.get(name='sponsor'))

        models.Sponsor.objects.create(
            user=user, 
            qualifications=request.POST.get('qualifications'), 
            organisation_name=request.POST.get('organisation_name'), 
            certificate=request.POST.get('certificate')
        )

        return redirect('sign_in')
    
    return render(request, 'authentication/forms/s_form.html')