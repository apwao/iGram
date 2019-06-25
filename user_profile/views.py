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
            created_profile = form.save(commit=False)
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
    profile_photos=Profile.objects.filter()
    all_user_photos=Image.objects.filter(editor=current_user.id)
    return render(request, 'profile.html',{'profile_photos':profile_photos})