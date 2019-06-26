from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views



#..............

urlpatterns=[
    url(r'^create_post/$', views.new_post, name='create_post'),
    url(r'^$', views.timeline_images, name='view_posts'),
    url(r'^add_comment/(\d+)/$',views.add_comment, name='add_comment'),
    url(r'^search_user/$', views.search_user, name='search_user'),
    url(r'^like_post/(\d+)$', views.like_post, name="like_post" ),
    url(r'^follow/(\d+)/$',views.follow, name='follow'),
    url(r'^view_suggestions/$',views.view_suggestions, name='view_suggestions'),
]


