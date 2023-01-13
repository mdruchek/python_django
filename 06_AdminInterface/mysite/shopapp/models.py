from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    arhived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return '{lastname} {firstname}'.format(lastname=self.lastname, firstname=self.firstname)


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return 'Заказ {order_id}'.format(order_id=self.id)
