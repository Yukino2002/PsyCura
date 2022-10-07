from . import views
from django.urls.conf import include
from django.urls import path


app_name = 'Users'


urlpatterns = [
    path('sign-out/', views.sign_out, name='sign_out'), 
    path('p/home/', views.p_home, name='p_home'), 
    path('d/home/', views.d_home, name='d_home'), 
    path('s/home/', views.s_home, name='s_home'), 
    path('home/', views.home, name='home'), 
    path('d/pending/', views.doctors_pending, name='doctors_pending'), 
]