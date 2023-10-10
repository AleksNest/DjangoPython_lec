from django.core.management.base import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "Get user by id"

    # функция считывает с команды параметры и добавляет значения в словарь kwargs по заданному ключу
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')         # pk - Это id (primary key) #  извлекает из строки целое число и сохраняет в словарб kwargs по ключу id

    # обработчик
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']                               # pk = числу, которое было получено в стр 9
        user = User.objects.filter(pk=pk).first()       #получение всех записей User при фильтрации пользоателя по id . first - извлечение только первого пользователя из табл БД
        self.stdout.write(f'{user}')                # вывод в консоль пользователя
