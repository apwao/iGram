from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField



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
    likes=models.IntegerField(default=0)
    # editor=models.ForeignKey(User,on_delete=models.CASCADE, default=0)
    upload_date=models.DateTimeField(auto_now_add=True)
    
    
    def save_image(self):
        """
        save_image method to check whether an instance of image
        is successfully stored to the database
        """
        self.save()
        
    def delete_image(self):
        """
        delete_image method to remove an image from the database
        """
        self.delete()
        
    def update_image(self):
        """
        update_image method to replace an image and its details in the database
        """
        self.update()
        
    def __str__(self):
        return self.name
    
# class Profile(models.Model):
#     """
#     Class Profile to create a profile instance containing an image 
#     and bio
#     """
#     profile_photo=image=models.ImageField(upload_to = 'timeline/')
    