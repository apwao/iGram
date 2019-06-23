from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image


# Create your views here.
# @login_required
def timeline_images(request):
    """
    timeline_images view function to display uploaded images on the timeline
    """
    images=Image.objects.all()
    return render(request, 'timeline.html', {'images':images})

# @login_required(login_url='/accounts/login')
def new_post(request):
    """
    new_post function to display the image_upload form
    """
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            created_post = form.save(commit=False)
            # created_post.editor = current_user
            created_post.save()
        return redirect('view_posts')

    else:
        form = ImageForm()
    return render(request, 'create_post.html', {"form": form})
        


    