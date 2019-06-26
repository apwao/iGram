from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image,Comment,Followers
from user_profile.models import Profile
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login')
def timeline_images(request):
    """
    timeline_images view function to display uploaded images on the timeline
    """
    current_user=request.user
    images = Image.objects.all()
    all_comments=Comment.objects.all()
    try:
        
        profile_photo=Profile.objects.get(user_id=current_user.id)
    except:
        profile_photo = [1, 2, 3]
        print("Error occured")
    user_name=current_user.username
    all_users = User.objects.all()
    
    all_followed=Followers.objects.filter(user_id=current_user.id)
    
    return render(request, 'timeline.html', {'images':images ,'all_comments':all_comments, 'all_users':all_users ,"profile_photo":profile_photo, "user_name":user_name, "all_followed":all_followed})

@login_required(login_url='/accounts/login')
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
        
@login_required(login_url='/accounts/login')
def add_comment(request, image_id):
    """
    add_comment view function to enable a user to comment on a post
    """
    current_user = request.user
    if request.method == 'POST' and request.POST['user_comments']:
        comment=request.POST.get('user_comments')
        new_comment= Comment.objects.create(comment=comment,image_id=image_id)
        
    return redirect(timeline_images)
    
def search_user(request):
   profile = Profile.objects.all() # get all profiles saved in the db
   if 'user_name' in request.GET and request.GET["user_name"]:
       search_term = request.GET.get("user_name")
       print(search_term)
       search_results = User.objects.filter(username__icontains=search_term)
       print(search_results)
       user_id = None
       for i in search_results:
        #    print(i.id)
           user_id = i.id
    #    print(type(user_id))
       profile_search_info = Profile.objects.filter(user_id=user_id)
       
    #    for i in profile_search_info:
    #        print(i.bio)
       
        

       message = f"{search_term}"

       return render(request, 'search_results.html',{"message":message,"profile":profile, 'profile_search_info':profile_search_info})

   else:
       message = "Please input a name in the search form"
       return render(request, 'search_results.html',{"message":message})
   
def like_post(request, image_id):
    """
    """
    print('$' * 20)
    print("Iam clicked", "Am no.", image_id)
    image = Image.objects.get(id=image_id)

    image.likes = image.likes + 1

    image.save()
    return redirect(timeline_images)

def follow(request,user_id):
    """
    """
    # if 'user_id' in request.GET and request.GET['user_id']:
    current_user = request.user.id
    new_follow=Followers.objects.create(to_follow_id=user_id, user_id=current_user)
    
    
    
    return render(request, 'timeline.html',{"current_user":current_user})
    
    
    
def view_suggestions(request):
    """
    """
    images=Image.objects.all()
    current_user = request.user.id
    all_users = User.objects.all()
    
    return render(request, 'suggestions.html',{"images":images, 'all_users':all_users})