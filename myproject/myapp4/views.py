import logging

from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from .models import User
from django.core.files.storage import FileSystemStorage         #для сохранения изображений

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':                    #проверка  на получение post или  get запроса
        form = UserForm(request.POST)               # создали форму, наполненными данными введенными пользователь в форму при нажатии кнопки отправить
        if form.is_valid():
            name = form.cleaned_data['name']        # извлечение данных из формы
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()                       # создали форму на основе пустого экземпляра класса
    return render(request, 'myapp4/user_form.html', {'form': form})


# приер применения виджетов в форме
def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp4/many_fields_form.html',  {'form': form})


# для записи вводимых данных из формы в БД
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


#для сохранения изображений загпужаемых из поля формы
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)           #извечение POST - текста, FILES - байт
        if form.is_valid():
            image = form.cleaned_data['image']                  #извлекаем изображение(байты)
            fs = FileSystemStorage()
            fs.save(image.name, image)                          #сохрани по имени image.name объект image(изображение )
    else:
        form = ImageForm()                                      # формируе пустую форму
    return render(request, 'myapp4/upload_image.html', {'form': form})
