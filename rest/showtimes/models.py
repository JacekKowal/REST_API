from django.db import models
from movielist.models import Movie


class Screening(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_screenings', on_delete=models.CASCADE)
    date = models.DateTimeField()

class Cinema(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    movies = models.ManyToManyField(Screening, related_name='cinema_screening')



