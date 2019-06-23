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
        
    def test_save_profile(self):
        """
        test_save_profile method to check whether an instance of profile
        is successfully stored to the database
        """
        self.profile1.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_profile(self):
        """
        test_delete_profile to check whether an instance of profile
        is successfully deleted from the database once it has been stored
        """
        self.profile1.save_profile()
        self.profile1.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)<1)
        
    def test_update_profile(self):
        """
        test_update_profile method to check for the successful replacement of
        a profile in the database with a new profile
        """
        self.profile1.save_profile()
        toUpdate=Profile.objects.filter(bio='Amazing').update(bio="Bleeeh")
        self.assertEquals(toUpdate,1)