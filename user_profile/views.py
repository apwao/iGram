from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from images.models import Image

# Create your views here.
@login_required(login_url='/accounts/login/')
def create_profile(request):
    """
    """
    current_user = request.user 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # if Profile.objects.filter(user_profile_photo=current_user.id):
            #     existing_user_profile = Profile.objects.filter(user_profile_photo=current_user.id)
            #     print(existing_user_profile)
                
            #     print('-' * 10)
            #     # print(form.cleaned_data['bio'], existing_user_profile.bio)
                
            #     # created_profile = form.save(commit=False)
            #     # created_profile.user_profile_photo = current_user.id
            #     new_image = form.save(commit=False)
            #     # new_image.save()
            #     form = ProfileForm(request.FILES)
            #     print('^*' * 20)
            #     print(form.is_valid())
            #     form.update()
                
                
            #     existing_user_profile.update(bio=form.cleaned_data['bio'])
                
                
            # else:
            created_profile = form.save(commit=False)
            created_profile.user_profile_photo = current_user.id
            created_profile.save()
                
        return redirect('view_profile')
    
    else:
        form=ProfileForm()
    return render(request, 'profile_form.html',{'form':form})

@login_required(login_url='/accounts/login/')
def view_profile(request):
    print(request)
    """
    """
    current_user=request.user
    profile_photos=Profile.objects.filter(id=current_user.id)
    all_user_photos=Image.objects.filter(editor=current_user.id)
    return render(request, 'profile.html',{'profile_photos':profile_photos})

