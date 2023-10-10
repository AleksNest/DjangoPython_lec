from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)                # Ссылаемся на класс автора , каскадное удаление - при удалении автора удаляем все его посты

    def __str__(self):
        return f'Title is {self.title}'

    # метод для вывода только первых 8 слов контента
    def get_summary(self):
        words = self.content.split()            #формируем список из слов
        return f'{" ".join(words[:8])}...'     # вывод только первых 8 слов