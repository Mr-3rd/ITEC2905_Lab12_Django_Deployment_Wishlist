from django.db import models

# Create your models here.

class Place(models.Model):
    # Can set DB options for the data column
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        # Useful information for the developer
        return f'{self.name} visited? {self.visited}'


    
    

