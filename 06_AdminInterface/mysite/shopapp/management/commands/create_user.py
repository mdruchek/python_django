from django.core.management import BaseCommand
from shopapp.models import User


class Command(BaseCommand):
    """
    Создаёт пользователя
    """

    def handle(self, *args, **options):
        self.stdout.write('Создание пользователя')
        user, created = User.objects.get_or_create(firstname=input('Введите имя пользователя: '))
        if created:
            self.stdout.write(self.style.SUCCESS(f'Пользователь {user.firstname} создан'))
        else:
            self.stdout.write(self.style.WARNING('Пользователь с таким именем уже существует'))
