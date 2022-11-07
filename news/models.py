from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", null=True)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Новости спорта"
        verbose_name_plural = "Новости спорта"
        ordering = ['id']

class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
        ordering = ['id']