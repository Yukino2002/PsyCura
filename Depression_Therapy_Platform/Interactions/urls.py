from . import views
from django.urls.conf import include
from django.urls import path


app_name = 'Interactions'


urlpatterns = [
    path("book-appointment",views.book_appointment,name="book_appointment")
    
]