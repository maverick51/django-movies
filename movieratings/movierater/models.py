from django.db import models


# Create your models here.
class Rater(models.Model):
    age = models.IntegerField()
    gender = models.IntegerField()
    occupation = models.IntegerField()
    zip_code = models.CharField(max_length=10)


class Movies(models.Model):
    movie_title = models.CharField(max_length=50)
    genres = models.CharField(max_length=20)


class Ratings(models.Model):
    rater_ob = models.ForeignKey(Rater)
    movie_ob = models.ForeignKey(Movies)
    rating = models.IntegerField()
    time_stamp = models.DateTimeField()
