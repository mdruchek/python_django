from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    content = models.TextField(verbose_name='Содержание', max_length=10000)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_editing = models.DateTimeField(auto_now=True)
    activity = models.BooleanField(verbose_name='Активно', default=True)


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
