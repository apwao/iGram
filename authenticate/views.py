from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.models import User 
from images.views import timeline_images


# Create your views here.
# def signup(request):
#     """
#     signup function to enable a user to signup to the application and be allowed
#     to log in after activating the account through a link
#     """
#     if request.method == 'POST': # if the request is a post
#         form=SignUpForm(request.POST) # create an instance of SignUpForm and pass in the post request values
#         if form.is_valid(): # if the form is validated,
#             user=form.save(commit=False) # save form but don't commit it to the database yet
#             user.is_active = False # If the user doesn't own an account yet, add them to the database
#             user.save()
#             current_site = get_current_site(request) # gets the domain name and human-readable name for a specific website
#             mail_subject = 'Activate your Instagram account.' # subject for the account activation email to be sent to user
#             message=render_to_string('acc_active_email.html',{ # call the render_to string and pass in the template to be rendered and the context
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(mail_subject,message,to=[to_email])
#             email.send()
            
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html',{'form': form})





def signup(request):
   if request.method == 'POST':         # if the request is a post
       form = SignUpForm(request.POST)  # create an instance of SignUpForm and pass in the post request values
       if form.is_valid():               # if the form is validated,
           user = form.save(commit=False) # save form but don't commit it to the database yet
           user.is_active = True          # If the user doesn't own an account yet, add them to the database
           user.save()   
           return render(request, 'activate.html')                  
        #    current_site = get_current_site(request)     # gets the domain name and human-readable name for a specific website
        #    mail_subject = 'Activate your Instagram account.' # subject for the account activation email to be sent to user
        #    message = render_to_string('acc_active_email.html', {
        #        'user': user,
        #        'domain': current_site.domain,
        #        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        #        'token':account_activation_token.make_token(user),
        #    })                                                       # call the render_to string and pass in the template to be rendered and the context
        #    to_email = form.cleaned_data.get('email')
        #    email = EmailMessage(
        #                mail_subject, message, to=[to_email]
        #    )
        #    email.send()
        # #    user.is_active = True
        # #    user.save()
        # #    login(request, user)
           
           
        # #    return render(request, 'registration/login.html')
        #    return HttpResponse('An email has been sent to you. Click on the link to activate your account')

   else:
       form = SignUpForm()
   return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
   try:
       uid = force_text(urlsafe_base64_decode(uidb64))
       user = User.objects.get(pk=uid)
   except(TypeError, ValueError, OverflowError, User.DoesNotExist):
       user = None
   if user is not None and account_activation_token.check_token(user, token):
       user.is_active = True
       user.save()
       login(request, user)
       # return redirect('home')
       return render(request,'activate.html')
   else:
       return HttpResponse('Activation link has expired')
    
