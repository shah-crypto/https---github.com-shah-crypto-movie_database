from django import forms
from django.core.files.images import ImageFile
from django.db import models
from django.db.models import fields
from django.db.models.enums import TextChoices
from django.db.models.fields.files import ImageFieldFile
from django.forms import widgets
from django.forms.fields import DateField, ImageField
from django.forms.widgets import ClearableFileInput, DateInput, DateTimeInput, FileInput, NumberInput, TextInput, Textarea, URLInput, Widget
from .models import Movie

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'name',
            'description',
            'genre',
            'rating',
            'year_of_release',
            'director',
            'cast',
            'link'
        ]
        widgets = {
            'name' : TextInput(attrs={
                'class':'form-control',
                'placeholder':'eg. The Shawshank Redemption'
            }),
            'description' : Textarea(attrs={
                'class':'form-control',
                'placeholder':'eg. Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                'required':True
            }),
            'rating' : NumberInput(attrs={
                'class':'form-control',
                'min':0.0,
                'max':5.0,
                'step':0.1,
                'placeholder':'eg 4.1'
            }),
            'preview_image': ClearableFileInput(attrs={
                'class':'form-control'
            }),
            'movie_image': ClearableFileInput(attrs={
                'class':'form-control'
            }),
            'year_of_release' : NumberInput(attrs={
                'class':'form-control',
                'min':1950,
                'max':2021,
                'step':1,
                'placeholder':'eg. 2014'
            }),
            'director' : TextInput(attrs={
                'class':'form-control',
                'placeholder':'eg. Frank Darabon'
            }),
            'cast' : TextInput(attrs={
                'class':'form-control',
                'placeholder':'eg. Tim Robbins, Morgan Freeman, Bob Gunton'
            }),
            'link' : URLInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'eg. https://www.netflix.com/in/title/70005379'
            })
        }