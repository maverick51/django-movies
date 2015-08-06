from django.shortcuts import render
import datetime
from .models import Rater, Movie, Rating


# Create your views here.
def each_individual_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    return render(request, 'movierater/each_individual_movie.html',
                  {'movie': movie})


def each_individual_user(request, rater_id):
    user = Rater.objects.get(pk=rater_id)

    return render(request, 'movierater/each_individual_user.html',
                  {'user': user})


def top_20_movies_rated(request):
    movies = Movie.objects.all()[:20]
    return render(request, 'movierater/top_20_movies_rated.html', {'movies': movies})
