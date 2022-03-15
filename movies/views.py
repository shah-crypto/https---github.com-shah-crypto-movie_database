from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Movie
from django.db.models import Q
from django.views.generic import TemplateView,ListView,DetailView
from django.shortcuts import get_object_or_404
from random import shuffle
from .forms import AddMovieForm

# Create your views here.
class MovieTemplateView(TemplateView):
    template_name = 'base.html'

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(MovieListView,self).get_context_data(**kwargs)
        context['all_movies'] = Movie.objects.filter(popular=True,approved=True).random(12)
        context['romance_movies'] = Movie.objects.filter(genre='romance',approved=True).random(8)
        context['superhero_movies'] = Movie.objects.filter(genre='superhero',approved=True).random(8)
        return context

class RomanceMovieListView(ListView):
    model = Movie
    template_name = 'rom_movies.html'
    
    def get_context_data(self):
        all_romance_movies = Movie.objects.filter(genre='romance',approved=True)
        all_romance_movies_list = list(all_romance_movies)
        shuffle(all_romance_movies_list)
        context = {}
        context['all_romance_movies_list'] = all_romance_movies_list
        return context

class SuperheroMovieListView(ListView):
    model = Movie
    template_name = 'superhero_movies.html'
    
    def get_context_data(self):
        all_superhero_movies = Movie.objects.filter(genre='superhero',approved=True)
        all_superhero_movies_list = list(all_superhero_movies)
        shuffle(all_superhero_movies_list)
        context = {}
        context['all_superhero_movies_list'] = all_superhero_movies_list
        return context

# class SuperheroMovieListView(ListView):
#     model = Movie
#     queryset = Movie.objects.filter(genre='superhero',approved=True)
#     template_name = 'superhero_movies.html'
#     context_object_name = 'all_superhero_movies'
    
class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movie_detail.html'

def MovieSearchView(request):
    if request.method == 'GET':
        query = request.GET.get('q').strip()
        submitbutton= request.GET.get('submit')

        if query != '':
            lookups= Q(name__icontains=query)
            results= Movie.objects.filter(lookups,approved=True).distinct()
            search_context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'searchresults.html', search_context)
        else:
            return render(request, 'searchresults.html')
    else:
        return render(request, 'searchresults.html')

def AddMovieView(request):
    context = {}
    if request.method == 'POST':
        form = AddMovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddMovieForm()
    context['form'] = form
    return render(request,'add_movie.html',context)