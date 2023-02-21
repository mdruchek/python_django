from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
