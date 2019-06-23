from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    """
    Class ImageTestClass to test the functionality and instantiation
    of class Image
    """
    
    def setUp(self):
        """
        setUp method to create an instance of Image
        class to be used during testing
        """
        
        self.image1=Image(image_name="Amazing",image_caption="Candid Photography",likes="50",comments="Pure talent")
    def tearDown(self):
        """
        tearDown method to create an clear the database after tests for each class are run
        """
        Image.objects.all().delete()

    def test_instance(self):
        """
        test_instance method to check for the correct creation of 
        an instance of Image
        """
        self.assertTrue(isinstance(self.image1,Image))
        
    def test_save_image(self):
        """
        test_save_image method to check whether an instance of image
        is successfully stored to the database
        """
        self.image1.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_delete_image(self):
        """
        test_delete_image to check whether an instance of image
        is successfully deleted from the database once it has been stored
        """
        self.image1.save_image()
        self.image1.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images)<1)
        
    def test_update_image(self):
        """
        test_update method to check for the successful replacement of
        an image in the database with a new image
        """
        self.image1.save_image()
        toUpdate=Image.objects.filter(image_name='image1').update(image_name="image2")
        self.assertEquals(toUpdate,1)