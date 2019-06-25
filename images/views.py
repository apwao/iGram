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
    # images = ["1", "2"]
    # images=Image.objects.all()
    images = Image.objects.all()
    print('->' * 30)
    # print(images)
    print(type(images))
    for i in images:
        print(i.image)
        # for j in i:
        #     print(i.image)
    return render(request, 'timeline.html', {'images':images})

# @login_required(login_url='/accounts/login')
def new_post(request):
    """
    new_post function to display the image_upload form
    """
    current_user = request.user
    current_user_name=current_user.username
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            created_post = form.save(commit=False)
            created_post.editor = current_user.id
            created_post.save()
        return redirect(timeline_images)

    else:
        form = ImageForm()
    return render(request, 'create_post.html', {"form": form, 'current_user_name':current_user_name})
        

def add_comment(request):
    """
    add_comment view function to enable a user to comment on a post
    """
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.editor = current_user.id
            comment.comments=form.field.value()
            comment.save()
            
    # else:
    #     form = CommentForm
    return render(request, 'timeline.html',{'form':form})
    
    