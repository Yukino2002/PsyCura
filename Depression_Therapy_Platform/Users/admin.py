from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Sponsor)
admin.site.register(Appointment)
admin.site.register(Forum)
admin.site.register(Log)