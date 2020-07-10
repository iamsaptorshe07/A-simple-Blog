from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
# Create your views here.
def signup(request):
    if request.method == 'POST':
        try:
            user = User()
            user.name=request.POST['name']
            user.email=request.POST['email']
            user.gender=request.POST['gender']
            if User.objects.filter(email=user.email).exists():
                messages.warning(request,'User Already Exist with this email address')
                return redirect('signup')
            else:
                user.set_password(request.POST['password'])
                user.save()
                messages.success(request,"Your account has been created")
                return redirect('login')
        except  Exception as problem:
            messages.error(request,'{}'.format(problem))
            return redirect('signup')
    else:
        return render(request,'signup.html')

def userlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Successfully Loggedin')
            return redirect('/')
    return render(request,'login.html')


def userLogout(request):
    try:
        auth.logout(request)
        messages.success(request,'Successfully Logged Out')
        return redirect('/')
    except Exception as problem:
        messages.success(request,'Sorry, Internal Problem Occured')
        return redirect('/')