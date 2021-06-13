from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Movie
from django.views.generic import TemplateView,ListView,DetailView
from django.shortcuts import get_object_or_404

# Create your views here.
class MovieTemplateView(TemplateView):
    template_name = 'base.html'

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(MovieListView,self).get_context_data(**kwargs)
        context['all_movies'] = Movie.objects.all().random(12)
        context['romance_movies'] = Movie.objects.filter(genre='romance').random(8)
        context['superhero_movies'] = Movie.objects.filter(genre='superhero').random(8)
        return context

class RomanceMovieListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(genre='romance')
    template_name = 'rom_movies.html'
    context_object_name = 'all_romance_movies'

class SuperheroMovieListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(genre='superhero')
    template_name = 'superhero_movies.html'
    context_object_name = 'all_superhero_movies'
    
class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movie_detail.html'
