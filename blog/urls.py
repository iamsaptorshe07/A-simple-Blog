"""autotechprogrammer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views 

urlpatterns = [
 path('',views.home,name='index'),
 path('myprofile',views.myprofile,name='myprofile'),
 path('blogwritter',views.blogWritter,name='blogwritter'),
 path('editpost/<str:id>',views.editpost,name='editpost'),
 path('deletepost/<str:id>',views.deletepost,name='deletepost'),
 path('searchContent',views.searchContent,name='SearchContent'),
 path('techblog',views.techblog,name='techblog'),
 path('automobileblog',views.automobileblog,name='automobileblog'),
 path('educationblog',views.educationblog,name='educationblog'),
 path('others',views.others,name='others'),
 path('postcomment',views.postComment,name='postcomment'),
 path('<str:slug>',views.blogPost,name='blogPost'),
]
