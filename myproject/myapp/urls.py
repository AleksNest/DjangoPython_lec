from django.urls import path
from . import views             # получаем доступ к views

#соединяем маршруты и представления
urlpatterns = [
    path('', views.index, name='index'),        # вызов по пути ''(127.0.0.1) функции index и даем имя index
    path('about/', views.about, name='about'),
]