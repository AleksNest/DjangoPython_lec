from django.db import models


# создаем табл User сос толбцами, поле id Dg добавляет автоматом
class User(models.Model):
    name = models.CharField(max_length=100)     # фимя пользователя ормат - набор букв
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()                 #формат - целое число

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


# создаем табл Product сос толбцами, поле id Dg добавляет автоматом
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)     # максимальная разрядность целой части - 8 разрядов, дробной - 2 разряда
    description = models.TextField()
    image = models.ImageField(upload_to='products/')                #хранит ссылки на изображение в каталоге products


# создаем табл  Заказ сос толбцами, поле id Dg добавляет автоматом
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)    # заказчик ссылается на пользователя, при удалении пользователя - удаляются все его заказы
    products = models.ManyToManyField(Product)                      # один продукт может находиться в нескольких заказах и разные заказы могут содержать один и тот же продукт
    date_ordered = models.DateTimeField(auto_now_add=True)          # при создании заказа автоматом создается время заказа
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


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