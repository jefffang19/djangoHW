from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_user, name='search_user'),
    path('movies', views.search_movie, name='search_movie'),
    path('insert_rating', views.insert_rating, name='insert_rating'),
    path('delete_rating', views.delete_rating, name='delete_rating'),
    path('update_rating', views.update_rating, name='update_rating'),
]