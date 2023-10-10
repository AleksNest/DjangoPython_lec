from django.core.management.base import BaseCommand

from my_app2.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):

        user = User(name='Mykle', email='Mykle@example.com', password='secret', age=45)   # создаем экземпляр User
        user.save()                 # создание экземпляра и сохраняем
        self.stdout.write(f'{user}')                # вывод в консоль пользователя
