from .decorators import unauthenticated_user
from Users import models
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import Group
import sys
sys.path.append('..')


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


@unauthenticated_user
def sign_in(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html')

    if request.method == 'POST':
        user = authenticate(
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )

        if user is not None:
            login(request, user)
            group = request.user.groups.all()[0].name
            
            if group == 'patient':
                return redirect('Users:p_home')
            elif group == 'doctor':
                return redirect('Users:d_home')
            elif group == 'sponsor':
                return redirect('Users:s_home')
            else:
                return redirect('Users:home')
        else:
            return render(request, 'sign_in.html')


@unauthenticated_user
def sign_up(request):
    return render(request, 'sign_up.html')


@unauthenticated_user
def p_sign_up(request):
    if request.method == 'GET':
        return render(request, 'p_form.html')

    elif request.method == 'POST':
        user = get_user_model().objects.create_user(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            age=request.POST.get('age'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone'),
            gender=request.POST.get('gender'),
            password=request.POST.get('password')
        )

        user.groups.add(Group.objects.get(name='patient'))

        patient = models.Patient.objects.create(
            user=user,
            past_medication=request.POST.get('medfile')
        )

        return redirect('sign_in')


@unauthenticated_user
def d_sign_up(request):
    return render(request, 'd_sign_up.html')


@unauthenticated_user
def s_sign_up(request):
    return render(request, 's_sign_up.html')

