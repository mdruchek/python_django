from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('автор'))
    content = models.TextField(max_length=1000, verbose_name=_('содержание'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'))

    class Meta:
        verbose_name_plural = _('блоги')
        verbose_name = _('блог')


class BlogImage(models.Model):
    image = models.ImageField(upload_to='files/', blank=True, verbose_name=_('изображение'))
    blog = models.ForeignKey(Blog, on_delete=CASCADE, verbose_name=_('блог'))

    class Meta:
        verbose_name_plural = _('изображения для блогов')
        verbose_name = _('изображение для блога')
