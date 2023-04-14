from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    balance = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name=_('Баланс'))

    class Meta:
        verbose_name = _('Профиль пользователя')
        verbose_name_plural = _('Профили пользователей')


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Название товара'))
    description = models.CharField(max_length=100, verbose_name=_('Описание товара'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Стоимость'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')


class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    products = models.ManyToManyField(Product, verbose_name='Продукты')

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')


class Stocks(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Название'))
    description = models.CharField(max_length=200, verbose_name=_('Описание'))
    promo_code = models.CharField(max_length=10, verbose_name=_('Промокод'))
    discount = models.IntegerField(default=0, verbose_name=_('Скидка'))

    class Meta:
        verbose_name = _('Скидка')
        verbose_name_plural = _('Скидки')


class Offer(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name=_('Продукт'))
    discount = models.IntegerField(default=0, verbose_name=_('Скидка'))

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Предложение')
        verbose_name_plural = _('Предложения')


class Shop(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Название'))
    address = models.CharField(max_length=100, verbose_name=_('Адрес'))

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural =_('Магазины')
