# Import the forms and the Place model
from django import forms
from .models import Place

# create the class for the form object
class NewPlaceForm(forms.ModelForm):
    # Create the magic by creating the Meta class
    class Meta:
        model = Place
        # must be spelled fields
        fields = ('name','visited')