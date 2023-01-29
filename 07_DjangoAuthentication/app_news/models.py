from django.db import models
from django.contrib.auth.models import User


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    content_comment = models.TextField(verbose_name='Содержание', max_length=200)
    date_creation = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey('NewsModel', on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)


class NewsModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    title = models.CharField(verbose_name='Заголовок', max_length=30)
    content_news = models.TextField(verbose_name='Содержание', max_length=1000)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
