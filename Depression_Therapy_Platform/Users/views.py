from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse


def sign_in(request):
    return render(request, 'Users/sign_in.html')