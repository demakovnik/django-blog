import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'password']
    email = models.EmailField('email address', unique=True, null=False)
    birth_date = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=60, null=False, unique=True)
    first_name = models.CharField(max_length=60,  blank=True)
    last_name = models.CharField(max_length=60, blank=True)


    def __str__(self):
        return self.username
