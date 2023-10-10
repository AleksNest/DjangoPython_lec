from django.core.management.base import BaseCommand

from my_app2.models import User


class Command(BaseCommand):
    help = "Get all users"

    # обработчик
    def handle(self, *args, **kwargs):
        users = User.objects.all()   #получение всех записей User из БД
        self.stdout.write(f'{users}')                # вывод в консоль пользователя
