from django.contrib import admin
from .models import Rater
from .models import Movie
from .models import Rating

# Register your models here.

# admin.site.register(Rater)
# admin.site.register(Movies)
# admin.site.register(Ratings)


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender', 'occupation', 'zip_code']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie_title', 'genres']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rater', 'movie', 'rating', 'time_stamp']


admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
