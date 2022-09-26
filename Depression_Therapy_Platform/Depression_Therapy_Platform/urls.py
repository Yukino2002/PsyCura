from django.contrib import admin
from django.urls import path
from . import views
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('users/', include('Users.urls')),
]