from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('cats/<int:catid>/', categories),  # http://127.0.0.1:8000/cats/1/
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('posts/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', NewsCategory.as_view(), name='category'),
]
