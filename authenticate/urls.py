from django.conf.urls import url
from . import views
# from django.contrib.auth import views
from django.conf import settings 

urlpatterns  = [
     # url('^signup/', views.register, name='register'),
     url(r'^$', views.signup, name='signup'),
     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       views.activate, name='activate'),
     
]