from django.contrib import admin

# Register your models here.
from app.models import User, Movie, Actor, Genre, CashReport, Rating, InterestingFacts, Comment

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(CashReport)
admin.site.register(Rating)
admin.site.register(InterestingFacts)
admin.site.register(Comment)