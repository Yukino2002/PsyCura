from django.db import models
import sys
sys.path.append("..")
from Users.models import CustomUser, Patient, Doctor


class Transaction(models.Model):
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    amount = models.PositiveIntegerField(default=0)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + ' ' + str(self.time) + ' ' + str(self.amount) + ' ' + str(self.patient.user.first_name) + ' ' + str(self.doctor.user.first_name)
    
    def transfer(self):
        self.patient.wallet_balance -= self.amount
        self.doctor.wallet_balance += self.amount

        