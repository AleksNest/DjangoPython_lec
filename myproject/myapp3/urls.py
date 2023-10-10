from django.urls import path
from .views import hello, HelloView, year_post, MonthPost, post_detail, my_view, TemplIf, view_for, index, about  # получаем доступ к views
from .views import author_posts, post_full

#соединяем маршруты и представления
urlpatterns = [
    path('hello/', hello, name='hello'),                         # путь связывает представление как функцию
    path('hello2/', HelloView.as_view(), name='hello2'),          # путь связывает представление как класс
    path('posts/<int:year>/', year_post, name='year_post'),         # year = целому числу из адресной строки и вызывается представление year_post
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),  # year = целому числу, month = целому числу из адресной строки вызывается метод класс  MonthPost.as_view()
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),   # slag:slag -> спецкоманда/ переменная, которо йприсваивается эта команда
    path('', my_view, name="index"),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name="templ_for"),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>',  author_posts, name='author_posts'),
    path('post/<int:post_id>',  post_full, name='post_full'),
]