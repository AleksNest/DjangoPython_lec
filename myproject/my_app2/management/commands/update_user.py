from django.core.management.base import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "update name by id"

    # функция считывает с команды параметры и добавляет значения в словарь kwargs по заданному ключу
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')         # pk - Это id (primary key) #  извлекает из строки команды целое число и сохраняет в словарь kwargs по ключу id
        parser.add_argument('name', type=str, help='User name')       #  извлекает из строки команды и сохраняет  в словарь kwargs  по ключу name

# обработчик
    def handle(self, *args, **kwargs):                  # обработка запроса
        pk = kwargs['pk']                               # pk = числу, которое было получено в стр 9
        name = kwargs['name']                            # name = строке, которое было получено в стр 10
        user = User.objects.filter(pk=pk).first()       #получение одного пользователя по id
        user.name = name
        user.save()
        self.stdout.write(f'{user}')                # вывод в консоль пользователя
