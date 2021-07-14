from django.urls import path
from .views import MovieTemplateView,MovieListView,MovieDetailView,RomanceMovieListView,SuperheroMovieListView,MovieSearchView
urlpatterns = [
    path('',MovieListView.as_view(),name='home-page'),
    path('romance/',RomanceMovieListView.as_view(),name='rom-movies_page'),
    path('superhero/',SuperheroMovieListView.as_view(),name='superhero_movies_page'),
    path('movie/<int:pk>',MovieDetailView.as_view(),name='movie-details'),
    path('search/',MovieSearchView,name='movie-search'),
]
