from django.http import HttpResponse            #возвращает HTTP ответы
from django.http import JsonResponse            #возвращает в виде JSON объекта
from django.shortcuts import render             # функция для работы с шаблонами
from django.shortcuts import get_object_or_404  # при обращении к БД, если нет ответа , то возвращает код 404 пользователю
from django.views import View
from django.views.generic import TemplateView  # класс для создания представления с особенностями  (для представления стр 50)

from .models import Author, Post                # импорт моделей


# Функция для вывода ответа на страницу браузера
def hello(request):
    return HttpResponse("Hello from function")              # возвращает объект headers для браузера


# Класс для вывода ответа на страницу браузера
class HelloView(View):              # наследуется от класса View
    def get(self, request):         # get - запрос
        return HttpResponse("Hello from class")             # возвращает объект headers для браузера


def year_post(request, year):
    text = ''
    # формируем статьи за год
    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = ''
        return HttpResponse(f'Posts from {year}/{month}<br>{text}')


def post_detail(request, year, month, slug):
    # Формируем статьи за год и месяц по идентификатору
    # Пока обойдемся без запросов к БД
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Заголовок",
        "content": "Контент 2 "
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})
    #  Возвращаем Json объект в браузер, преобразует post в json включая кодировку Utf-8


#проброс контекста в шаблон
def my_view(request):
    context = {"name": "Jonh"}
    return render(request, "myapp3/my_template.html", context)      #запрос - путь к шаблону - контекст - словарь


class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"          #имя шаблона, template_name - зарезервированное имя

    def get_context_data(self, **kwargs):           #зарезервированное имя метода
        context = super().get_context_data(**kwargs)       #обращение к родительскому шаблону, извлекаем контекст из него и добавляем свои данные ниже
        context['massage'] = "привет мир"
        context['number'] = 5
        return context

def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'должен': 'синий',
        'знать': 'голубой',
        'где': 'желтый',
        'сидит': 'черный',
        'фазан': 'белый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}      # пробрасываем словарь по двум ключам
    return render(request, "myapp3/templ_for.html", context)  # запрос - путь к шаблону - контекст - словарь

#представления для дочерних шаблонов
def index(request):
    return render(request, "myapp3/index.html")

def about(request):
    return render(request, "myapp3/about.html")


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)                #при существующем id автор будет извлечен иначе возвратит код 404
    posts = Post.objects.filter(author=author).order_by('-id')[:5] #находит посты по автору и отсортировать по id в обратном порядке 5 записей
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})

