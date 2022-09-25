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