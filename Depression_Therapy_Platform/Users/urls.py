from . import views
from django.urls.conf import include
from django.urls import path


app_name = 'Users'


urlpatterns = [
    path('', views.sign_in, name='sign_in'),
]