from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    print("moviesie",list(Movie.objects.all()))
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    print("template data,",template_data)
    print("movies",list(movies))
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

def show(request, id):
    movie = get_object_or_404(Movie, id=id)
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    return render(request, 'movies/show.html',
                  {'template_data': template_data})

def create_review(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/create_review.html', {'movie': movie})

def edit_review(request, id, review_id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/edit_review.html', {'movie': movie})
