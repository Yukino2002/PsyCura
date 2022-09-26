from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse


def profile(request):
    return render(request, 'Users/profile.html')


