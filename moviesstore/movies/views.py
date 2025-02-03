from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie

def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

def show(request, id):
    movie = get_object_or_404(Movie, id=id)
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    return render(request, 'movies/show.html',
                  {'template_data': template_data})

# ✅ Add this function to fix the error
def create_review(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/create_review.html', {'movie': movie})

# ✅ Add this function to avoid another potential error
def edit_review(request, id, review_id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/edit_review.html', {'movie': movie})
