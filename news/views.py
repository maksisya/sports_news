from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

def index(request):
    posts = News.objects.all()
    cats = Categories.objects.all()
    parameters = {
        'posts': posts,
        'title': 'Главная страница',
        'menu': menu,
        'cats': cats,
        'cat_selected': 0,
    }
    return render(request, 'news/index.html', context=parameters)

def about(request):
    return render(request, 'news/about.html', {'menu': menu, 'title': 'О нас'})

def categories(request, catid):
    return HttpResponse(f"<h1>Новости по категориям, страница № {catid}</h1>")

def contact(request):
    return HttpResponse('<h1>Страница контактов</h1>')

def login(request):
    return HttpResponse('<h1>Страница входа</h1>')

def show_post(request, post_id):
    return HttpResponse(f"<h1>Отображение статьи с id = {post_id}</h1>")

def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
    cats = Categories.objects.all()
    parameters = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'cats': cats,
        'cat_selected': cat_id,
    }

    return render(request, 'news/index.html', context=parameters)

# def error_404(request, excpeption):
#     return HttpResponseNotFound('<h1>Страница не найдена!</h1>')