from django.shortcuts import render
from django.http import HttpResponse
from .decorators import allowed_users
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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
    return render(request, 'Users/staff/profile.html', {'staff':request.user})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def doctors_pending(request):
    return render(request, 'Users/staff/d_pending.html', {'staff':request.user})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def doctors_approved(request):
    return render(request, 'Users/staff/d_approved.html', {'staff':request.user})


@login_required(login_url='sign_in')
@allowed_users(allowed_users=['admin', 'staff'])
def doctors_banned(request):
    return render(request, 'Users/staff/d_banned.html', {'staff':request.user})


@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    return redirect('sign_in')