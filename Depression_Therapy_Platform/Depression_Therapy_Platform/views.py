from Users import models
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
import sys
sys.path.append('..')


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('Users:profile')
        else:
            return render(request, 'sign_in.html')

    elif request.method == 'POST':
        pass


def sign_up(request):
    return render(request, 'sign_up.html')


def p_sign_up(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('Users:profile')
        else:
            return render(request, 'p_sign_up')

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

        patient = models.Patient.objects.create(
            user=user,
            past_medication=request.POST.get('medfile')
        )

        return redirect('sign_in')


def d_sign_up(request):
    return render(request, 'd_sign_up.html')


def s_sign_up(request):
    return render(request, 's_sign_up.html')
