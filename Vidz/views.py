from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video
from django.db import models
from .decorators import unauthenticated_user, allowed_user,admin_only
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.


# @login_required(login_url='login')
def Home(request):    
    video = Video.objects.all().order_by('-time')

    
    context={
        'video':video ,
    }
    
    return render(request, 'Vidz/home.html',context)

# @unauthenticated_user
def userLog(request):    
    
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            username = request.POST.get('name')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print('were here')
                return redirect('home')

            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {'form': form}
        return render(request, 'Vidz/login.html', context)
    
    
    
# @unauthenticated_user
def userReg(request):
    form = CreateUserForm()
    
    context = {'form': form}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
           
            
            messages.success(request, 'Account created for ' + username)
            return redirect('login')
    return render(request, 'Vidz/register.html', context)


def LogoutPage(request):
    logout(request)
    return redirect('login')

def video(request, pk):    
    video_all = Video.objects.all()    
    video = Video.objects.get(id=pk)
    context={
        'video':video,
        'video_all': video_all,
    }
    
    return render(request, "Vidz/video.html", context)

def videoForm(request):
    form = VideoForm()    
    if request.method == 'POST':
        form = VideoForm(request.POST)        
        if form.is_valid():
            print("were hhere")
            form.save()
            return redirect('video')
           
    context={'form':form}
    return render(request, "Vidz/video_form.html", context)