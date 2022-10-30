from django.db import models


class Session(models.Model):
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    report = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.date + ' ' + self.time + ' ' + self.forum.name

