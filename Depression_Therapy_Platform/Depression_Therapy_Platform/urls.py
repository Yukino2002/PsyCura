from django.contrib import admin
from django.urls import path
from views import *
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    
]