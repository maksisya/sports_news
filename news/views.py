from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
# Create your views here.
# superuser: login admin, pass 123

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Войти", 'url_name': 'login'},
]


def index(request):
    posts = News.objects.filter(is_published=True)
    # cats = Categories.objects.all()
    parameters = {
        'posts': posts,
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0,
    }
    return render(request, 'news/index.html', context=parameters)


def about(request):
    return render(request, 'news/about.html', {'menu': menu, 'title': 'О нас'})


def categories(request, catid):
    return HttpResponse(f"<h1>Новости по категориям, страница № {catid}</h1>")


def contact(request):
    return HttpResponse('<h1>Страница контактов</h1>')


def addpage(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                News.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'news/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def login(request):
    return HttpResponse('<h1>Страница входа</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'news/post.html', context=context)


def show_category(request, cat_slug):
    posts = News.objects.filter(cat__slug=cat_slug, is_published=True)
    if len(posts) == 0:
        return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
    # cats = Categories.objects.all()
    parameters = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'cat_selected': cat_slug,
    }

    return render(request, 'news/index.html', context=parameters)

# def error_404(request, excpeption):
#     return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
