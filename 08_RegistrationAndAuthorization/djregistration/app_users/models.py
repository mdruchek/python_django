from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=20, blank=True)
    number_news = models.IntegerField(default=0)
