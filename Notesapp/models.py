from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class notes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


