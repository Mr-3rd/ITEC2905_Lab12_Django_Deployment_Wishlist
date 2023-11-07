from django.shortcuts import render, redirect
from .models import Place
# import the forms object - NOTE - look at where forms.py is!
from .forms import NewPlaceForm

# Create your views here.
def place_list(request):

    if request.method == 'POST':
        # create a form if the post method is called
        form = NewPlaceForm(request.POST)
        # create a place model object from the form data
        place = form.save()
        # Check if the form is valid and then save the place to the DB
        if form.is_valid():
            place.save()
            # after saving to DB reload the page
            return redirect('place_list') 

    # Setup our list of places using dJango builtins on the Place model developed in models.py
    # filter out visited places, and sort by the name if the place
    places = Place.objects.filter(visited=False).order_by('name')
    #add the new form into the place list view: HTML data
    new_place_form = NewPlaceForm()
    # return by rendering the wishlist website to display the places
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

# create the places visited page view
def places_visited(request):
    visited = Place.objects.filter(visited=True).order_by('name')
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

# Create the function to build the about page
def about(request):
    # Create the author and about content
    author = "Mr. 3rd"
    about = "A website designed in django which allows for a user to save visited places!"
    # render the ab out page with content
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})
