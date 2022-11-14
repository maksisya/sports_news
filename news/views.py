from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
# Create your views here.
# superuser: login admin, pass 123

from .utils import *


class NewsHome(DataMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def index(request):
#     posts = News.objects.filter(is_published=True)
#     # cats = Categories.objects.all()
#     parameters = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'menu': menu,
#         'cat_selected': 0,
#     }
#     return render(request, 'news/index.html', context=parameters)

@login_required
def about(request):
    return render(request, 'news/about.html', {'menu': menu, 'title': 'О нас'})


def categories(request, catid):
    return HttpResponse(f"<h1>Новости по категориям, страница № {catid}</h1>")


def contact(request):
    return HttpResponse('<h1>Страница контактов</h1>')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'news/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

# def addpage(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'news/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def login(request):
    return HttpResponse('<h1>Страница входа</h1>')


class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#     post = get_object_or_404(News, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'news/post.html', context=context)


class NewsCategory(DataMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=self.kwargs['cat_slug'])
        # context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        # context['menu'] = menu
        # context['cat_selected'] = self.kwargs['cat_slug']
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

# def show_category(request, cat_slug):
#     posts = News.objects.filter(cat__slug=cat_slug, is_published=True)
#     if len(posts) == 0:
#         return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
#     # cats = Categories.objects.all()
#     parameters = {
#         'posts': posts,
#         'title': 'Отображение по рубрикам',
#         'menu': menu,
#         'cat_selected': cat_slug,
#     }
#
#     return render(request, 'news/index.html', context=parameters)

# def error_404(request, excpeption):
#     return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
