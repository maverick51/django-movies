from django.shortcuts import render
import datetime
from .models import Rater, Movie, Rating


# Create your views here.
def each_individual_movie(request):
    movies = Movie.objects.all().order_by('-id')
    page_load = datetime.datetime.now()

    return render(request, 'movierater/each_individual_movie.html',
                  {'movies': movies, 'page_load': page_load})


def each_individual_user(request):
    user = Rater.objects.all().order_by('-id')
    page_load = datetime.datetime.now()

    return render(request, 'movierater/each_individual_user.html',
                  {'user': user, 'page_load': page_load})


def top_20_movies_rated(request):
    rating = Rating.objects.all().order_by('-time_stamp')
    page_load = datetime.datetime.now()

    return render(request, 'movierater/top_20_movies_rated.html',
                  {'rating': rating, 'page_load': page_load})
