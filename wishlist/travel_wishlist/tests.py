from django.test import TestCase

# import the reverse function to search urls
from django.urls import reverse

# import the Place object
from .models import Place


# Create your tests here.

class TestHomePage(TestCase):

    def test_homepage_empty_list_message(self):
        # User reverse to lookup the url by the name given in the urls.py file name
        homepage_url = reverse('place_list')
        # make a response to the website by calling the self in 
        # TestCase to use an internal client to get the homepage
        response = self.client.get(homepage_url)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertContains(response, 'You have no places in your list') 

# new class to test the fixtures.py files
class TestWishList(TestCase):

    fixtures = ['test_places']

    def test_wishlist_not_visited(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')
        self.assertNotContains(response, 'Moab')

# test for no places in the visited page:
class TestVisitedPage(TestCase):

    def test_visited_page_empty_list_message(self):
        # User reverse to lookup the url by the name given in the urls.py file name
        visited_url = reverse('places_visited')
        # make a response to the website by calling the self in 
        # TestCase to use an internal client to get the visited page
        response = self.client.get(visited_url)
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'You have not visited any places in your list') 

# test for the places that have been visited:
# new class to test the fixtures.py files
class TestVisitedList(TestCase):

    fixtures = ['test_places']

    def test_wishlist_visited_only(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')
        self.assertContains(response, 'San Francisco')
        self.assertContains(response, 'Moab')