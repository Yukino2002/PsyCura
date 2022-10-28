from django.db import models


class Forum(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=None)
    number_patients = models.IntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    report = models.CharField(max_length=100, blank=True, null=True)

    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return self.date + ' ' + self.time + ' ' + self.forum.name

# class Time_Table(models.Model):
#     day = models.CharField(max_length=10,choices=(('Sun','Sunday'),('Mon','Monday'),('Tue','Tuesday'),('Wed','Wednesday'),('Thu','Thursday'),('Fri','Friday'),('Sat','Saturday')))
#     time = models.TimeField()
#     doctor = models.ForeignKey('Users.Doctor',on_delete = models.CASCADE)

#     class Meta:
#         unique_together = (("day","time","doctor"),)

#     def __str__(self):
#         return self.day + ' ' + self.time + ' ' + self.doctor
    
    
        

