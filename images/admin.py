from django.contrib import admin

# Register your models here.
from .models import Image,Comment,Followers

admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Followers)