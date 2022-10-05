from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

@login_required(login_url='sign_in')
@allowed_users(allowed_users=['patient'])
def p_home(request):
    return render(request, 'Users/patient/home.html')


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['doctor'])
def d_home(request):
    return render(request, 'Users/doctor/home.html')


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['sponsor'])
def s_home(request):
    return render(request, 'Users/sponsor/home.html')


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def home(request):
    return render(request, 'Users/staff/home.html')