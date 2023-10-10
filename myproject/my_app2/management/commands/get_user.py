from django.core.management.base import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "Get user by id"

    # функция считывает с команды параметры и добавляет значения в словарь kwargs по заданному ключу
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')         # id извлекает из строки команды целое число и сохраняет в словарб kwargs по ключу id

    # обработчик
    def handle(self, *args, **kwargs):                  # обработка запроса
        id = kwargs['id']                               # id = числу, которое было получено в стр 10
        user = User.objects.get(id=id)       #получение всех записей User по Id
        self.stdout.write(f'{user}')                # вывод в консоль пользователя
