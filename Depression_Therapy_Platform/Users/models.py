from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
import sys
sys.path.append("..")


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password address')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password address')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(
        18), MaxValueValidator(100)], null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(
        ('M', 'Male'), ('F', 'Female'), ('NB', 'Non-Binary')), null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    username = 'first_name' + 'last_name'
    objects = CustomUserManager()

    def _str_(self):
        return self.email


class Forum(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=None)
    number_patients = models.IntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, primary_key=True)
    wallet_balance = models.PositiveIntegerField(default=0)
    past_diseases = models.CharField(max_length=1000, blank=True, null=True)
    past_medication = models.FileField()

    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Doctor(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, primary_key=True)
    wallet_balance = models.PositiveIntegerField(default=0)
    qualifications = models.CharField(max_length=1000, blank=True, null=True)
    certificate = models.FileField(default=None)
    specialization = models.CharField(default='a', max_length=30, choices=(("Abnormal", "Abnormal"),
                                                                           ("Biopsychologist",
                                                                            "Biopsychologist"),
                                                                           ("Cognitive",
                                                                            "Cognitive"),
                                                                           ("Developmental",
                                                                            "Developmental"),
                                                                           ("Personality",
                                                                            "Personality"),
                                                                           ("Forensic",
                                                                            "Forensic"),
                                                                           ("Industrial-organizational",
                                                                           "Industrial-organizational")
                                                                           )
                                      )
    experience = models.PositiveIntegerField(default=0, blank=True, null=True)
    rating = models.PositiveIntegerField(default=0, blank=True, null=True)
    fee = models.PositiveIntegerField(default=500, blank=True, null=True)
    is_approved = models.CharField(max_length=10, choices=(
        ('A', 'Approved'), ('P', 'Pending'), ('B', 'Banned')), default='P')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Sponsor(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, primary_key=True)
    qualifications = models.CharField(max_length=1000, blank=True, null=True)
    organisation_name = models.CharField(max_length=100, blank=True, null=True)
    certificate = models.FileField()
    is_approved = models.CharField(max_length=10, choices=(
        ('A', 'Approved'), ('P', 'Pending'), ('B', 'Banned')), default='P')

    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Log(models.Model):
    body = models.CharField(max_length=1000)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body + ' ' + self.patient.user.first_name + ' ' + self.patient.user.last_name


class Appointment(models.Model):
    date = models.DateField(default=None)
    start_time = models.TimeField(default=None)
    end_time = models.TimeField(default=None)
    approved = models.BooleanField(default=False)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.date) + ' ' + str(self.patient.user.first_name) + ' ' + str(self.doctor.user.first_name)
