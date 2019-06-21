from django.db import models

# Create your models here.
class Profile(models.Model):
    """
    Class Pofile to create an instance of a user profile
    """
    bio=models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)
    
    def save_profile(self):
        """
        save_image method to check whether an instance of image
        is successfully stored to the database
        """
        self.save()