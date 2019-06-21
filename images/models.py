from django.db import models

# Create your models here.
class Image(models.Model):
    """
    Class Image to create an image instance alongside all its
    details
    """
    image=models.ImageField(upload_to = 'timeline/')
    image_name=models.CharField(max_length=100)
    image_caption=models.TextField()
    comments=models.TextField()
    likes=models.IntegerField()
    
    
    def save_image(self):
        """
        test_save_image method to check whether an instance of image
        is successfully stored to the database
        """
        self.save()