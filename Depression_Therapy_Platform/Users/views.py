from django.shortcuts import render
from django.contrib.auth import get_user_model
from datetime import datetime
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


