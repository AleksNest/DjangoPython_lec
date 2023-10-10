from django.core.management.base import BaseCommand

from my_app2.models import Author, Post


class Command(BaseCommand):
    help = "Generate fake author and posts"

    # функция считывает с команды параметры и добавляет значения в словарь kwargs по заданному ключу
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')         # count - это количество записей в таблиц, сохраняет count в словарь kwargs по ключу count

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')                                     # сохраняет в переменную из словаря kwargs по ключу 'count'
        for i in range(1, count+1):
            author = Author(name=f'Name{i}', email=f'mail{i}@mail.ru')  # в переменную создаем экземпляры обьектов (записи в табл)
            author.save()
            self.stdout.write(f'{author}')
            for j in range(1, count+1):
                post = Post(
                    title=f'Tittle{j}',
                    content=f'Text from{author.name} {j} text',
                    author=author)
                post.save()
                self.stdout.write(f'{post}')



