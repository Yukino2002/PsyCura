from django.db import models
from Users.models import Doctor,Patient
 

# Create your models here.
class Time_Table(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.doctor.user.first_name + ' ' + self.doctor.user.last_name + ' ' + self.date + ' ' + self.time



    

