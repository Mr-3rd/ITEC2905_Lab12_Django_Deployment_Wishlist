from django.db import models

# import the model for django built in
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    # Can set DB options for the data column

    # add details for the user- not blank, set the action to occur for the user deletion 
    # cascade will delete all user associated details
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    
    notes = models.TextField(blank=True, null =True)
    date_visited = models.DateField(blank=True, null =True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null =True)

    #original data
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'

        notes_str = self.notes[100:] if self.notes else 'no notes'

        # Useful information for the developer
        return f'{self.name} visited? {self.visited} on {self.date_visited}. Notes: {notes_str}... Photo: {photo_str}'



    
    

