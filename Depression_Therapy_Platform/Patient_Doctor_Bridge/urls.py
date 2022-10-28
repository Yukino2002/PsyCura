from . import views
from django.urls.conf import include
from django.urls import path

app_name = 'Patient_Doctor_Bridge'


urlpatterns = [
    path("book-appointment",views.book_appointment,name="book_appointment"),
    path("appointments",views.appointments,name="appointments")
    #path("Time-table/set",views.setTimeTable,name="set_time_table")
    
]