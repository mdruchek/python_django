from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)


class BlogImage(models.Model):
    image = models.ImageField(upload_to='files/', blank=True)
    blog = models.ForeignKey(Blog, on_delete=CASCADE)
