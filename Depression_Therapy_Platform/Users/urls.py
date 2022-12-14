from . import views
from django.urls.conf import include
from django.urls import path


app_name = 'Users'


urlpatterns = [
    path('p/profile', views.p_home, name='p_home'),
    path("p/doctors",views.p_doctors, name="p_doctors"),
    path('p/doctors/<d_id>',views.p_doctor_card, name="p_doctor_card"),
    path('p/appointments/future',views.p_appointments_future, name="p_appointments_future"),
    path('p/appointments/past',views.p_appointments_past, name="p_appointments_past"),
    path('p/forums', views.p_forums, name='p_forums'),

    path('d/profile', views.d_home, name='d_home'), 
    path('d/appointments/future',views.d_appointments_future, name="d_appointments_future"),
    path('d/appointments/past',views.d_appointments_past, name="d_appointments_past"), 
    
    path('s/profile', views.s_home, name='s_home'), 
    
    path('profile', views.home, name='home'), 
    path('d-pending', views.doctors_pending, name='doctors_pending'), 
    path('d-approved', views.doctors_approved, name='doctors_approved'), 
    path('d-banned', views.doctors_banned, name='doctors_banned'), 
    path('d-update/<d_id>', views.doctor_update, name='doctor_update'), 
    path('s-pending', views.sponsors_pending, name='sponsors_pending'), 
    path('s-approved', views.sponsors_approved, name='sponsors_approved'), 
    path('s-banned', views.sponsors_banned, name='sponsors_banned'), 
    path('s-update/<s_id>', views.sponsors_update, name='sponsor_update'), 
    path('sign-out', views.sign_out, name='sign_out'), 
]