from django.core.validators import RegexValidator
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60, null=False)
    surname = models.CharField(max_length=60)
    email = models.EmailField(max_length=30, null=False, unique=True)
    birth_at = models.DateField(null=False)
    login = models.CharField(max_length=60, null=False, unique=True)
    password = models.CharField(
        null=False,
        max_length=128,
        validators=[
            RegexValidator(
                regex='^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                message='Password must be at least 8 characters long and contain at least one letter and one number'
            )
        ]
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = models.TextField()
    created_at = models.DateTimeField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
