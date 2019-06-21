from django.test import TestCase
from .models import Profile



# Create your tests here.
class ProfileTestClass(TestCase):
    """
    Class ImageTestClass to test the functionality and instantiation
    of class Image
    """
    
    def setUp(self):
        """
        setUp method to create an instance of Image
        class to be used during testing
        """
        
        self.profile1=Profile(bio="Amazing")
    def tearDown(self):
        """
        tearDown method to create an clear the database after tests for each class are run
        """
        Profile.objects.all().delete()

    def test_instance(self):
        """
        test_instance method to check for the correct creation of 
        an instance of Image
        """
        self.assertTrue(isinstance(self.profile1,Profile))
        
    