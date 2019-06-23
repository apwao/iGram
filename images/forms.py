from .models import Image
from django import forms

class ImageForm(forms.ModelForm):
    """
    Class ImageForm to process user input in terms of an image
    and its details
    """
    class Meta:
        model=Image
        exclude=['editor','upload_date','likes','comments']
        
        
        