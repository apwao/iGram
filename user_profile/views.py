from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

# Create your views here.
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


def view_profile(request):
    """
    """
    return render(request, 'profile.html')