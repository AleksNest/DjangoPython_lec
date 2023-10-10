from django.urls import path
from .views import user_form, many_fields_form, add_user, upload_image

#соединяем маршруты и представления
urlpatterns = [
    path('user/add/', user_form, name='user_form'),                 # вывод поля для ввода данных напримере небольшого кол полей
    path('forms/', many_fields_form, name='many_fields_form'),       # вывод поля для ввода данных напримере большого кол полей

    # вывод поля для ввода данных напримере небольшого кол полей c записью данных полей в БД
    path('user/', add_user, name='add_user'),

    #для загрузки изображения
    path('upload/', upload_image, name='upload_image'),
]