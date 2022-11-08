from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', categories),  # http://127.0.0.1:8000/cats/1/
    path('about/', about, name='about'),
    path('add_page/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('posts/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
]
