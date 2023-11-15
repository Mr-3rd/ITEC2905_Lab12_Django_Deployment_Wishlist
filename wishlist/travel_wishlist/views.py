from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
# import the forms object - NOTE - look at where forms.py is!
from .forms import NewPlaceForm, TripReviewForm
# add a logion decorator to ensure a user sees only their places
from django.contrib.auth.decorators import login_required
# include security to keep from changing visited places
from django.http import HttpResponseForbidden
# import django's messages package to display the update notification
from django.contrib import messages


# Create your views here.


@login_required
def place_list(request):

    if request.method == 'POST':
        # create a form if the post method is called
        form = NewPlaceForm(request.POST)
        # create a place model object from the form data
        place = form.save(commit=False)
        # collect the current user as the places user
        place.user = request.user
        # Check if the form is valid and then save the place to the DB
        if form.is_valid():
            place.save()
            # after saving to DB reload the page
            return redirect('place_list') 

    # Setup our list of places using dJango builtins on the Place model developed in models.py
    # filter out visited places, and sort by the name if the place
    # filtering the user allows the db to only show the current users places from the db
    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name')
    #add the new form into the place list view: HTML data
    new_place_form = NewPlaceForm()
    # return by rendering the wishlist website to display the places
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

@login_required
# create the places visited page view
def places_visited(request):
    visited = Place.objects.filter(visited=True).order_by('name')
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

@login_required
# Create the function to build the about page
def about(request):
    # Create the author and about content
    author = "Mr. 3rd"
    about = "A website designed in django which allows for a user to save visited places!"
    # render the ab out page with content
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})

@login_required
def place_visited(request, place_pk):

    if request.method == 'POST':

        # Method to search for one item - by Primary Key or ID
        # place = Place.objects.get(pk=place_pk)

        # Using the 404 option
        place = get_object_or_404(Place, pk=place_pk)

        # test if the user is the one that created the b item
        if place.user == request.user:
            place.visited = True
            # Change is not retained unless saved
            place.save()
        else:
            return HttpResponseForbidden()

    # I prefer to be directed to the visited places
    # return redirect('place_list')
    return redirect('places_visited')

@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)

    # add the code to get the place and display/modify the existing details

    # user permissions?
    if place.user != request.user:
        return HttpResponseForbidden()
    
    # Post Request? validate form and update model
    if request.method == 'POST':
        # create a new form with the data sent to update an instance of a place in the db
        form = TripReviewForm(request.POST, request.FILES, instance=place)

        if form.is_valid():
            form.save()
            messages.info(request, 'Trip information updated')
        else:
            messages.error(request, form.errors) #refine later
        
        return redirect('place_details', place_pk=place_pk)
    else:
        # Get Request? show place info and optional form
        # if place is not visited, do not show the form
        if place.visited:
            review_form = TripReviewForm(instance=place)
            return render(request, 'travel_wishlist/detail.html', {'place': place, 'review_form': review_form})
        else:
            return render(request, 'travel_wishlist/detail.html', {'place': place})


@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list') 
    else:
        return HttpResponseForbidden()
