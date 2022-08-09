from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = News.objects.all()
    return render(request, 'news/index.html', {'posts': posts, 'title': 'Главная страница', 'menu': menu})

def about(request):
    return render(request, 'news/about.html', {'menu': menu, 'title': 'О нас'})

def categories(request, catid):
    return HttpResponse(f"<h1>Новости по категориям, страница № {catid}</h1>")

# def error_404(request, excpeption):
#     return HttpResponseNotFound('<h1>Страница не найдена!</h1>')