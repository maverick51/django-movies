from django.db import models
from django.db.models import Avg

# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.IntegerField()
    zip_code = models.CharField(max_length=10)

    def get_all_movies(self):
        return self.rating_set.all()

    def __str__(self):
        return "Rater age: {};  Rater gender: {};  Rater occupation: {};  Rater Zip Code: {}".\
            format(self.age, self.gender, self.occupation, self.zip_code)


class Movie(models.Model):
    movie_title = models.CharField(max_length=75)
    genres = models.CharField(max_length=25)

    def avg_rating(self):
        rating = self.rating_set.aggregate(Avg('rating'))
        if rating == None:
            return 0
        else:
            return rating['rating__avg']

    def get_all_ratings(self):
        return self.rating_set.all()

    def __str__(self):
        return "Movie title: {};  Genre:  {}".format(self.movie_title, self.genres)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    time_stamp = models.IntegerField()

    def __str__(self):
        return "Rater:  {};  Movie:  {};  Rating:  {};  Time stamp:  {}"\
            .format(self.rater, self.movie, self.rating, self.time_stamp)
