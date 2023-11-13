# Import the forms and the Place model
from django import forms
from .models import Place
from django.forms import FileInput, DateInput

# create the class for the form object
class NewPlaceForm(forms.ModelForm):
    # Create the magic by creating the Meta class
    class Meta:
        model = Place
        # must be spelled fields
        fields = ('name','visited')

# create a custom date field to replace the default, text
class DateInput(forms.DateInput):
    input_type = 'date' 


class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput()
        }