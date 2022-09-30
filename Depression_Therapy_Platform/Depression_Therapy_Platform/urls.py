from django.contrib import admin
from django.urls import path
from . import views
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('p-sign-up/', views.p_sign_up, name="p_sign_up"),
    path('d-sign-up/', views.d_sign_up, name="d_sign_up"),
    path('s-sign-up/', views.s_sign_up, name="s_sign_up"),
    path('users/', include('Users.urls')),
]