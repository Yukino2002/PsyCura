from django.db import models
import sys
sys.path.append("..")
from Services.models import Forum
from django.core.validators import RegexValidator,MaxValueValidator,MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


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
    age = models.PositiveIntegerField(validators=[MinValueValidator(18),MaxValueValidator(100)],null=True,blank=True)
    gender = models.CharField(max_length=10,choices=(('M', 'Male'), ('F', 'Female'), ('NB', 'Non-Binary')),null=True,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=10,null=True,blank=True) 
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    username = 'first_name' + 'last_name'
    objects = CustomUserManager()

    def _str_(self):
        return self.email


class Patient(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    wallet_balance = models.PositiveIntegerField(default=0)
    past_diseases = models.CharField(max_length=1000,blank=True,null=True)
    past_medication = models.FileField()

    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Doctor(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    wallet_balance = models.PositiveIntegerField(default=0)
    qualifications = models.CharField(max_length=1000,blank=True,null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Sponsor(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    qualifications = models.CharField(max_length=1000,blank=True,null=True)
    organization_name = models.CharField(max_length=100,blank=True,null=True)
    approved = models.BooleanField(default=False)

    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name