from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views



#..............

urlpatterns=[
    url('^create_post/$', views.new_post, name='create_post'),
    url('^view_posts/$', views.timeline_images, name='view_posts'),
    url('^add_comment/$',views.add_comment, name='add_comment')
]
