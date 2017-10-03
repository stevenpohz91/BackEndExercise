from django.conf.urls import url
#whenever user requests something, you just want to give back
#some html response, a simple view (example)
#therefore, we need to import those view:
#. = current directory
from . import views

urlpatterns = [

#^ = start
#$ = end
#^$ is also saying whenever user is not requesting anything, it suppose to go to views, then look for the function call index
#the pattern below is any pattern
    url(r'^$',views.index, name='index'),


#/music/71/, where 71 is song ID
#this pattern "[0-9]+" is going to match any following integer, hence it means any combination of single integers, where it will be group together within the bracket "()" as a single ID
#we also need to connect to the view function
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]