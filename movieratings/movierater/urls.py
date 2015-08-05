from django.conf.urls import url


urlpatterns = [
    url(r'(?P<movie_id>[0-9]+)/', 'movierater.views.each_individual_movie', name='each_individual_movie'),
    url(r'(?P<rater_id>[0-9]+)/', 'movierater.views.each_individual_user', name='each_individual_user'),
    url(r'^$', 'movierater.views.top_20_movies_rated', name='top_20_movies_rated'),
]
