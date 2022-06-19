from typing import Text
from .models import *
from django.forms import ModelForm, TextInput


class MovieForm(ModelForm):
    model = Movie
    fields = ["title", "description"]
    widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input the movie'
        }),
        "description": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input the description'
        })
    }


class ReviewForm(ModelForm):
    model = Review
    fields = ["text"]
    widgets = {
        "text": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input the text'
        })
    }


class DirectorForm(ModelForm):
    model = Director
    fields = ["name"]
    widgets = {
        "name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input the name'
        })
    }
