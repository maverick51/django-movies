from django.contrib import admin
from .models import Rater
from .models import Movies
from .models import Ratings

# Register your models here.

# admin.site.register(Rater)
# admin.site.register(Movies)
# admin.site.register(Ratings)


class RaterAdmin(admin.ModelAdmin):
    list_display = ['age', 'gender', 'occupation', 'zip_code']


class MoviesAdmin(admin.ModelAdmin):
    list_display = ['movie_title', 'genres']


class RatingsAdmin(admin.ModelAdmin):
    list_display = ['rater_ob', 'movie_ob', 'rating', 'time_stamp']


admin.site.register(Rater, RaterAdmin)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Ratings, RatingsAdmin)
