from django.core.management.base import BaseCommand

from my_app2.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by author id"

    # функция считывает с команды параметры и добавляет значения в словарь kwargs по заданному ключу
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')         # шв - эсохраняет id из командной строки шв в словарь kwargs по ключу id

    # def handle(self, *args, **kwargs):
    #     pk = kwargs.get('pk')                                     # извлекает из словаря kwargs('pk') значение id и записывает в переменную id
    #     author = Author.objects.filter(pk=pk).first()               # записывает в переменную  author данные из табл author с указанным id, берем только первую по очереди строку с указанным id
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)              # записывает в переменную posts данные из табл Post с указанным author, берем все строки с данным author и пишем в список QuerySet []
    #         intro = f'All posts of {author.name}\n'
    #        # text = '\n'.join(post.content for post in posts)             #формируем строку из значений столбца content из табл Post выбранного id author
    #         text = posts
    #         self.stdout.write(f'{intro}{text}')                     # печать в консоль


# другой вариант реализации кода строки 13 - 20
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')                                     # извлекает из словаря kwargs('pk') значение id и записывает в переменную id
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.content for post in posts)        # формируем строку из значений столбца content из табл Post выбранного id author
        self.stdout.write(f'{intro}{text}')                     # печать в консоль
        self.stdout.write(f'{posts}')
