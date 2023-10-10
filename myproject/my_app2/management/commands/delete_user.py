from django.core.management.base import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "delete user by id"

    # функция считывает с команды параметры и добавляет значения в словарь kwargs по заданному ключу
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')         # pk - Это id (primary key) #  извлекает из строки команды целое число и сохраняет в словарь kwargs по ключу id


# обработчик
    def handle(self, *args, **kwargs):                  # обработка запроса
        pk = kwargs['pk']                               # pk = числу, которое было получено в стр 9
        user = User.objects.filter(pk=pk).first()       #получение одного пользователя по id
        if user is not None:
            user.delete()                               # удаление всей строки по id из БД
        self.stdout.write(f'{user}')                # вывод в консоль пользователя
