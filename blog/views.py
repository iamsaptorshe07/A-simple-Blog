from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import *
from django.contrib import  messages
# Create your views here.
def home(request):
    post = BlogPost.objects.all().order_by('-timestamp')
    context = {
        'Post':post,
    }
    return render(request,'index.html',context)

def blogPost(request, slug):
    user = request.user
    if user.is_authenticated:        
        post = BlogPost.objects.get(slug=slug)
        comments = BlogComment.objects.filter(post=post,parent=None)
        replies = BlogComment.objects.filter(post=post).exclude(parent=None)
        context = {
            'Post':post,
            'Comments':comments,
            'Replies':replies,
        }
        return render(request,'blogpost.html',context=context)
    else:
        messages.warning(request,'Please Log in to view the content')
        return redirect('/')

def searchContent(request):
    search = request.GET.get('search')
    postTitle = BlogPost.objects.filter(title__icontains=search) # Use double underscore to search anything
    postContent = BlogPost.objects.filter(content__icontains=search)
    post = postTitle.union(postContent)
    context = {
        'Post':post
    }
    return render(request,'search.html',context=context)

def products(request):
    return render(request,'affilate.html')


def techblog(request):
    post = BlogPost.objects.filter(category='Tech').order_by('-timestamp')
    context = {
        'Post':post
    }
    return render(request,'index.html',context)


def automobileblog(request):
    post = BlogPost.objects.filter(category='Automobile').order_by('-timestamp')
    context = {
        'Post':post
    }
    return render(request,'index.html',context)


def educationblog(request):
    post = BlogPost.objects.filter(category='Education').order_by('-timestamp')
    context = {
        'Post':post
    }
    return render(request,'index.html',context)


def others(request):
    post = BlogPost.objects.filter(category='Others').order_by('-timestamp')
    context = {
        'Post':post
    }
    return render(request,'index.html',context)


def postComment(request):
    if request.method=='POST':
        user = request.user
        postId = request.POST.get('post_id')
        post = BlogPost.objects.get(id=postId)
        comment = request.POST.get('comment')
        parentcomment = request.POST.get('parentcomment')
        if parentcomment=="":    
            blogcomment = BlogComment(post=post,user=user,comment=comment)
        else:
            parent = BlogComment.objects.get(id=parentcomment)
            blogcomment = BlogComment(post=post,user=user,comment=comment,parent=parent)
        blogcomment.save()
        messages.success(request,'Successfully added your comment')
        return redirect('/{}'.format(post.slug))
            
    else:
        return HttpResponse('Page not found')
    


def blogWritter(request):
    if request.method == 'POST':
        title = request.POST['title']
        thumbnail = request.FILES['thumbnail']
        category = request.POST['category']
        tags = request.POST['tags']
        content = request.POST['content']
        user = request.user
        slug = title
        blogpost = BlogPost(
            title=title,thumbnail=thumbnail,category=category,content=content,tags=tags,writer=user,slug=slug)
        blogpost.save()
        messages.success(request,'Blog Posted')
        return redirect('/')
    else:
        user = request.user
        if user.is_authenticated:
            return render(request,'blogwritter.html')
        else:
            messages.warning(request,'Login Required to post blog')
            return redirect('/accounts/login')

def myprofile(request):
    user = request.user
    blogpost = BlogPost.objects.filter(writer=user)
    context = {
        'Post':blogpost,
    }
    return render(request,'myprofile.html',context=context)

def editpost(request,id):
    if request.method == 'POST':
        from datetime import datetime
        post = BlogPost.objects.get(id=request.POST['id'])
        post.tags = request.POST['tags']
        post.content = request.POST['content']
        post.title=request.POST['title']
        post.category = request.POST['category']
        post.timestamp = datetime.now()
        post.save()
        messages.success(request,'Edited Successfully')
        return redirect('/')
    else:        
        post = BlogPost.objects.get(id=id)
        context = {
            'post':post
        }
        return render(request,'editpost.html',context=context)
    
    
def deletepost(request,id):
    post = BlogPost.objects.get(id=id)
    post.delete()
    messages.success(request,'post deleted')
    return redirect('/')
