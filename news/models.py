from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title