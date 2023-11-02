from django.db import models

from authentication.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = models.TextField()
    created_at = models.DateTimeField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
