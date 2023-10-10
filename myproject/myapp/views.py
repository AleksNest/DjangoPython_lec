from django.shortcuts import render
from django.http import HttpResponse # Возвращает ответ от сервера клиенту(пользователю)


def index(reguest):
    return HttpResponse("Привет, МИР")


def about(reguest):
    return HttpResponse("Обо мне")

