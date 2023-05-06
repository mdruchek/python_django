from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Содержание')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = '-published_at',
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Room(models.Model):
    type = models.CharField(max_length=20, verbose_name='Тип')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return self.type


class TypeHousing(models.Model):
    type = models.CharField(max_length=50, verbose_name='Тип')

    class Meta:
        verbose_name = 'тип жилья'
        verbose_name_plural = 'типы жилья'

    def __str__(self):
        return self.type


class Housing(models.Model):
    address = models.CharField(max_length=200, verbose_name='Адрес')
    type = models.ForeignKey(TypeHousing, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Жильё'
        verbose_name_plural = 'Жильё'

    def get_absolute_url(self):
        return reverse('housing_detail', args=[str(self.id)])

    def __str__(self):
        return self.type.type


