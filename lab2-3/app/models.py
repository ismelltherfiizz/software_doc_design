from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CashReport(models.Model):
    budget = models.CharField(max_length=200)
    gross = models.CharField(max_length=200)

    def __str__(self):
        return self.gross


class InterestingFacts(models.Model):
    information = models.CharField(max_length=200)

    def __str__(self):
        return self.information


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField
    cashReport = models.ForeignKey(CashReport, on_delete=models.CASCADE)
    interestingFacts = models.ForeignKey(InterestingFacts, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthplace = models.CharField(max_length=200)
    birthdate = models.DateField(max_length=200)
    photo = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.first_name


class User(models.Model):
    nickname = models.CharField(max_length=200)
    birthdate = models.DateField(max_length=200)
    email = models.CharField(max_length=200)
    watchlist = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class Genre(models.Model):
    typeOfGenre = models.CharField(max_length=200)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.typeOfGenre


class Rating(models.Model):
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment