from django.core.management.base import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "Get user with age greater <age>"

    # функция считывает с команды параметры и добавляет значения в словарь kwargs по заданному ключу
    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')         # извлекает из строки команды целое число из введенгой команды и сохраняет в словарь kwargs по ключу age

    # обработчик
    def handle(self, *args, **kwargs):                  # обработка запроса
        age = kwargs['age']                               # age = числу, которое было получено в стр 9
        user = User.objects.filter(age__gt=age)       #получить из столбца age все возраста, которые больше того значения, которое было получено в стр 9 (вели в  команде)
        self.stdout.write(f'{user}')                # вывод в консоль пользователя
