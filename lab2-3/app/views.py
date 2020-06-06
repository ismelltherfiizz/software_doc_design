import os
import re
from django.db.models import Sum
from django.http import HttpResponse, Http404

from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from app.models import Movie, CashReport, InterestingFacts, Actor, User, Genre, Rating, Comment


def movie_page(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    template = get_template('movie_page.html')
    html = template.render({'movie': movie})
    return HttpResponse(html)


def read_csv_file(request):

    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'generated.csv')
    with open(file_path, 'r+') as file:
        buffer = file.read()

    first = re.split(r'Cash Report\n', buffer)[1]
    sec = re.split(r'.*\n\nInteresting Facts\n', first)[0]
    cash_reports = sec.split('\n')
    for cash_report in cash_reports:
        cash_reports = cash_report.split(',')
        if cash_report != '':
            CashReport.objects.get_or_create(
                budget=cash_reports[0],
                gross=cash_reports[1]
            )

    first = re.split(r'Interesting Facts\n', buffer)[1]
    sec = re.split(r'.*\n\nMovie\n', first)[0]
    interesting_facts = sec.split('\n')
    for interesting_fact in interesting_facts:
        interesting_facts = interesting_fact.split(',')
        if interesting_fact != '':
            InterestingFacts.objects.get_or_create(
                information=interesting_facts[0]
            )

    first = re.split(r'Movie\n', buffer)[1]
    sec = re.split(r'.*\n\nActor\n', first)[0]
    movies = sec.split('\n')
    for movie in movies:
        movies = movie.split(',')
        if movie != '':
            Movie.objects.get_or_create(
                title=movies[0],
                year=movies[1],
                description=movies[2],
                cashReport_id=movies[3],
                interestingFacts_id=movies[4]
            )

    first = re.split(r'Actor\n', buffer)[1]
    sec = re.split(r'.*\n\nUser\n', first)[0]
    actors = sec.split('\n')
    for actor in actors:
        actors = actor.split(',')
        if actor != '':
            Actor.objects.get_or_create(
                first_name=actors[0],
                last_name=actors[1],
                birthplace=actors[2],
                birthdate=actors[3],
                photo=actors[4]
            )

    first = re.split(r'User\n', buffer)[1]
    sec = re.split(r'.*\n\nGenre\n', first)[0]
    users = sec.split('\n')
    for user in users:
        users = user.split(',')
        if user != '':
            User.objects.get_or_create(
                nickname=users[0],
                birthdate=users[1],
                email=users[2],
                watchlist=users[3],
                photo=users[4],
                movie_id=users[5]
            )

    first = re.split(r'Genre\n', buffer)[1]
    sec = re.split(r'.*\n\nRating\n', first)[0]
    genres = sec.split('\n')
    for genre in genres:
        genres = genre.split(',')
        if genre != '':
            Genre.objects.get_or_create(
                typeOfGenre=genres[0]
            )

    first = re.split(r'Rating\n', buffer)[1]
    sec = re.split(r'.*\n\nComment\n', first)[0]
    ratings = sec.split('\n')
    for rating in ratings:
        ratings = rating.split(',')
        if rating != '':
            Rating.objects.get_or_create(
                rating=ratings[0],
                user_id=ratings[1]
            )

    first = re.split(r'Comment\n', buffer)[1]
    comments = first.split('\n')
    for comment in comments:
        comments = comment.split(',')
        if comment != '':
            Comment.objects.get_or_create(
                comment=comments[0],
                user_id=comments[1]
            )

    return HttpResponse('<html><h1>SUCCESS</h1></html>')
