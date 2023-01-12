from shopapp.models import Product
from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Создаёт новые продукты
    """

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых продуктов')

    def handle(self, *args, **options):
        self.stdout.write('Создание продукта')
        total = options['total']
        for _ in range(total):
            product, created = Product.objects.get_or_create(name=input('Введите название продукта: '))
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создан продукт {product.name}'))
            else:
                self.stdout.write(self.style.WARNING('Продукт с таким названием уже есть'))
