from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')