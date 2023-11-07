from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'),
    # create a new url for a visited page
    path('visited', views.places_visited, name='places_visited'),

    path('about', views.about, name='about'),
]