from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from movielens.models import Movies, Ratings

def index(request):
    return HttpResponse('Welcome to my site')

def search_user(request):
    if request.method == 'GET':
        #.get() only return 1 data
        #use .filter() instead
        r = Ratings.objects.filter(user_id=request.GET['user_id'])
        
        return HttpResponse(r)

def search_movie(request):
    if request.method == 'GET':
        r = Movies.objects.get(pk=request.GET['movie_id'])

        return HttpResponse(r)


#csrf protection exception
@csrf_exempt
def insert_rating(request):
    if request.method == 'POST':
        r = Ratings.objects.create(user_id=request.POST['user_id'], \
                                    movie_id=request.POST['movie_id'], \
                                    rating=request.POST['rating'])
        r.save()
        return HttpResponse()

@csrf_exempt
def delete_rating(request):
    if request.method == 'POST':
        r = Ratings.objects.filter(user_id=request.POST['user_id'], \
                                    movie_id=request.POST['movie_id'], \
                                    rating=request.POST['rating'])
        r.delete()
        return HttpResponse()
