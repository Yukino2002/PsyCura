from django.db import models
import sys
sys.path.append("..")
from Users.models import Patient, Doctor, Sponsor


class Appointment(models.Model):
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    prescription = models.CharField(max_length=1000, blank=True, null=True)
    approved = models.BooleanField(default=False)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + ' ' + str(self.time) + ' ' + str(self.patient.user.first_name) + ' ' + str(self.doctor.user.first_name)


class Transaction(models.Model):
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    amount = models.PositiveIntegerField(default=0)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + ' ' + str(self.time) + ' ' + str(self.amount) + ' ' + str(self.patient.user.first_name) + ' ' + str(self.doctor.user.first_name)