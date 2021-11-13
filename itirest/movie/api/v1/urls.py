from django.urls import path
from .views import hello, movie_list , movie_create, movie_details, movie_delete, movie_update

urlpatterns = [
    path('helloapi/<str:key>', hello, name='hello'),
    path('api/v1/movies', movie_list, name='movies-index'),
    path('api/v1/movie/create', movie_create, name='movie-create'),
    path('api/v1/movie/<int:pk>', movie_details, name='movie-details'),
    path('api/v1/movie/delete/<int:pk>', movie_delete, name='movie-delete'),
    path('api/v1/movie/update/<int:pk>', movie_update, name='movie-update')
]