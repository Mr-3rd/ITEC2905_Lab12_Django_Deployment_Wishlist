from selenium.webdriver.chrome.webdriver import WebDriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):

    # perform setup
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()


    def test_title_homepage(self):
        # This will allow django to find the correct url of the current server
        self.selenium.get(self.live_server_url)
        self.assertIn('The World Explored - Travel Wishlist', self.selenium.title)

    
class AddPlaceTest(LiveServerTestCase):

    fixtures = ['test_places']

    # perform setup
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()

    def test_add_place(self):

        self.selenium.get(LiveServerTestCase)
        input_name = self.selenium.find_element_by_id('id_name')
        input_name.send_keys('Denver')
        add_button = self.selenium.find_element_by_id('add-place')
        add_button.click()

        # find the new place in the db by looking for pk 5
        denver = self.selenium.find_element_by_id('place-name-5')

        self.assertEqual('Denver', denver.text)

        self.assertIn('Denver', self.selenium.page_source)
        self.assertIn('New York', self.selenium.page_source)
        self.assertIn('Tokyo', self.selenium.page_source)

