from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'),
    # create a new url for a visited page
    path('visited', views.places_visited, name='places_visited'),

    path('about', views.about, name='about'),

    # create the path to updating a not visited place - note that the int allows for django to build a dynamic path
    path('place/<int:place_pk>/was_visited', views.place_visited, name='place_visited'),
]