from . import views
from django.urls.conf import include
from django.urls import path


app_name = 'Users'


urlpatterns = [
    path('p/home', views.p_home, name='p_home'), 
    path('d/home', views.d_home, name='d_home'), 
    path('s/home', views.s_home, name='s_home'), 
    path('home', views.home, name='home'), 
    path('d-pending', views.doctors_pending, name='doctors_pending'), 
    path('d-approved', views.doctors_approved, name='doctors_approved'), 
    path('d-banned', views.doctors_banned, name='doctors_banned'), 
    path('d-update/<d_id>', views.doctor_update, name='doctor_update'), 
    path('sign-out', views.sign_out, name='sign_out'), 
]