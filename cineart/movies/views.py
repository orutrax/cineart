from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cineart.movies.models import Movie


@login_required
def list_movies(request):
    """List of Movies view"""

    movies = Movie.objects.all()

    context = {
        "title": "Billboard",
        "movies": movies
    }

    return render(request, "movie/list.html", context)


@login_required
def detail_movie(request, pk):
    """Detail of a movie View"""

    movie = Movie.objects.get(id=pk)

    context = {
        "movie": movie
    }

    return render(request, "movie/detail.html", context)
