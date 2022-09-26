from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='sign_in')
def profile(request):
    return render(request, 'Users/profile.html')


