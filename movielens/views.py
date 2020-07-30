from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from movielens.models import Movies, Ratings

def index(request):
    return HttpResponse('Welcome to my site')

def search_user(request):
    if request.method == 'GET':
        #.get() only return 1 data
        #use .filter() instead
        r = Ratings.objects.filter(user_id=request.GET['user_id'])

        returnlist = []
        for i in r:
            d = { 'user_id' : i.user_id, 'movie_id' : i.movie_id, 'rating' : i.rating }
            returnlist.append(d)
        
        returndict = {'rating_list' : returnlist}
        return JsonResponse(returndict)

def search_movie(request):
    if request.method == 'GET':
        r = Movies.objects.get(pk=request.GET['movie_id'])

        d = {'movie_id' : r.movie_id, 'title' : r.title, 'genres' : r.genres}

        return JsonResponse(d)


#csrf protection exception
@csrf_exempt
def insert_rating(request):
    if request.method == 'POST':
        r = Ratings.objects.create(user_id=request.POST['user_id'], \
                                    movie_id=request.POST['movie_id'], \
                                    rating=request.POST['rating'])
        r.save()
        return HttpResponse('insert success')

@csrf_exempt
def delete_rating(request):
    if request.method == 'POST':
        r = Ratings.objects.filter(user_id=request.POST['user_id'], \
                                    movie_id=request.POST['movie_id'], \
                                    rating=request.POST['rating'])
        r.delete()
        return HttpResponse('delete success')

@csrf_exempt
def update_rating(request):
    if request.method == 'POST':
        r = Ratings.objects.filter(user_id=request.POST['user_id'], \
                                    movie_id=request.POST['movie_id'])
        r.update(rating = request.POST['rating'])
        return HttpResponse('update success')