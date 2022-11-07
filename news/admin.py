from django.contrib import admin

# Register your models here.

from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date_update', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(News, NewsAdmin)
admin.site.register(Categories, CategoriesAdmin)