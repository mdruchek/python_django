from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, verbose_name=_('пользователь'))
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name=_('аватарка'))

    class Meta:
        verbose_name = _('профиль пользователя')
