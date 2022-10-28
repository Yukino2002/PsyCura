from . import views
from django.urls.conf import include
from django.urls import path


app_name = 'Users'


urlpatterns = [
    path('p/profile', views.p_home, name='p_home'), 
    path('d/profile', views.d_home, name='d_home'), 
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
    path('forums', views.staff_forums, name='staff_forums'), 
]