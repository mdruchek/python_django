from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ["name", "price"]

    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание", null=False, blank=True)
    price = models.DecimalField(verbose_name="Цена", default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(verbose_name="Скидка", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return '{product_name} ({product_descr})'.format(product_name=self.name,
                                                         product_descr=self.description[0:5])


class Order(models.Model):
    delivery_address = models.TextField(verbose_name="Адрес доставки", null=True, blank=True)
    promocode = models.CharField(verbose_name="Промокод", max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Покупатель", on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, verbose_name="Выберите товары", related_name="orders")
