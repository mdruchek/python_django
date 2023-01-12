from django.core.management import BaseCommand
from shopapp.models import Product, Order


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help=u'Количество добавляемых продуктов')

    def handle(self, *args, **options):
        order = Order.objects.get(id=int(input('Введите номер заказа: ')))
        for _ in range(options['amount']):
            product = Product.objects.get(name=input('Введите название продукта: '))
            order.products.add(product)
            self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} добавлен в заказ {order.id}'))
