from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'


    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'image', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


    # пользовательская валидация входных данных в форме, методы должны начинаться с clean_имя-поля
    # метод должен генерировать исключение ValidationError(строка, которая будет появляться в форме)
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 220:
            raise ValidationError('Длина заголовка не должна превышать 220 символов!')
        return title
