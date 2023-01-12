from django.core.management import BaseCommand
from shopapp.models import User, Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Создание заказа')
        user = User.objects.get(firstname=input('Введите имя пользователя: '))
        order, created = Order.objects.get_or_create(
            delivery_address=input('Введите адрес доставки: '),
            promocode=input('Введите промокод: '),
            users=user
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Заказ {order.id} создан'))
