from django.shortcuts import render
movies = [
    {
        'id': 1, 'name': 'Inception', 'price': 12,
        'description': 'A mind-bending heist thriller.'
    },
    {
        'id': 2, 'name': 'Avatar', 'price': 13,
        'description': 'A journey to a distant world and the battle for resources.'
    },
    {
        'id': 3, 'name': 'The Dark Knight', 'price': 14,
        'description': 'Gothams vigilante faces the Joker.'
    },
    {
        'id': 4, 'name': 'Titanic', 'price': 11,
        'description': 'A love story set against the backdrop of the sinking Titanic.',
    },
]
def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

<<<<<<<< HEAD:moviesstore/movies/views.py
def show(request, id):
    movie = movies[id - 1]
    template_data = {}
    template_data['title'] = movie['name']
    template_data['movie'] = movie
    return render(request, 'movies/show.html',
                  {'template_data': template_data})
========
@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('home.show', id=id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'home/edit_review.html',
            {'template_data': template_data})
    elif request.method == 'POST' and
    request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('home.show', id=id)
    else:
        return redirect('home.show', id=id)
>>>>>>>> 9696fa6 (a little bit):moviesstore/home/views.py
