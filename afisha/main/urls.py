from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('movies', views.movies, name='Movies'),
    path('directors', views.directors, name='Directors'),
    path('reviews', views.reviews, name='Reviews')
]