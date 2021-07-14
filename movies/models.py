from django.db import models

# Create your models here.
from django.db import models
from django_random_queryset import RandomManager

GENRE_CHOICES = (
    ('action','Action'),
    ('adventure','Adventure'),
    ('comedy','Comedy'),
    ('crime and mystery','Crime & Mystery'),
    ('documentary','Documentary'),
    ('family','Family'),
    ('fantasy','Fantasy'),
    ('historical','Historical'),
    ('horror','Horror'),
    ('romance','Romance'),
    ('scientific fiction','Science fiction'),
    ('superhero','Superhero'),
    ('thriller','Thriller'),
    ('western','Western'),
)

class Movie(models.Model):
    objects = RandomManager()
    name = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(choices=GENRE_CHOICES,max_length=20)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    preview_image = models.ImageField(upload_to='photos/',null=True)
    movie_image = models.ImageField(upload_to='photos/')
    year_of_release = models.PositiveIntegerField()
    movie_time = models.TimeField()
    director = models.CharField(max_length=100)
    cast = models.TextField()
    link = models.URLField()
    popular = models.BooleanField(default=False)