from django.db import models


class Advertisements(models.Model):
    title = models.CharField(verbose_name='Заголовок объявления', max_length=100)
    descriptions = models.TextField(verbose_name='Описание', max_length=1000)
    price = models.FloatField(verbose_name='Цена', default=0)
    publication_start_date = models.DateTimeField(auto_now_add=True)
    publication_end_date = models.DateTimeField(blank=True, editable=True, default=None)
    author = models.ForeignKey('AdvertisementAuthor', verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ForeignKey('AdvertisementCategory', verbose_name='Категория', on_delete=models.CASCADE)
    type = models.ForeignKey('AdvertisementType', default=1, on_delete=models.CASCADE)
    number_views = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return '{id_adv}: {title_adv}'.format(id_adv=self.id, title_adv=self.title)


class AdvertisementAuthor(models.Model):
    name = models.CharField(verbose_name='Автор', max_length=50)
    email = models.CharField(verbose_name='email', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=16)

    def __str__(self):
        return '{name} / {email} / {phone}'.format(name=self.name,
                                                   email=self.email,
                                                   phone=self.phone)


class AdvertisementCategory(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=50)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(verbose_name='Тип объявления', max_length=50)

    def __str__(self):
        return self.name
