# from django.urls import path 
# from . import views 
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]

from django.contrib import admin
from django.urls import re_path
from blog import views as blog_views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^blog/$', blog_views.index, name='index'),
    re_path(r'^blog/(?P<post_id>[0-9]+)/$', blog_views.detail, name='detail'),	
]
