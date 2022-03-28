from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import UserRegisterForm, UserAuthForm, AddPhotoForm, ProfileForm
from .models import *
from django.db.models import Q


def basePage(request):
    form = UserAuthForm()
    if request.user.is_authenticated:
        print(request.user)
        user = User.objects.get(username = request.user)
        us = user.profile
        blogs = user.blogs.all()
        param = {'blogs': blogs,
                 'form': form,
                 'us': us}
    else:
        blogs = Blog.objects.all().order_by('-creation')[:9]
        param = {'blogs': blogs,
             'form': form,
             }

    return render(request,'base.html',param)


def register(request):
    if request.method == 'POST':
        userReg = UserRegisterForm(request.POST)
        if userReg.is_valid():
            userReg.save()
            user= User.objects.get(username = request.POST['username'])
            Profile(userProfile=user, emailProfile= request.POST['email'], slug = request.POST['username']).save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Ошибка регистрации')
    else:
        userReg = UserRegisterForm()
    param = {'userReg': userReg}
    return render(request,'register.html', param)


def userLogin(request):
    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserAuthForm()
    return render(request, 'login.html', {'form':form})


def logoutUser(request):
    logout(request)
    return redirect('/')


def addPhoto(request):
    if request.user.is_authenticated:
        if  request.method == 'POST':
            form = AddPhotoForm(request.POST,request.FILES)
            if form.is_valid():
                venue = form.save(commit=False)
                venue.user_id = request.user.id
                venue.save()
                return redirect('/')
        else:
            form = AddPhotoForm()
        return render(request,'add.html', {'form':form})


def viewBlog(request, slug):
    if request.user.is_authenticated:
        blog = User.objects.get(pk = request.user.id).blogs.get(slug=slug)
        return render(request,'blog.html', {'blog':blog})
    return HttpResponse('Ok')


def viewProfile(request, slug):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ProfileForm(request.POST)
        if form.is_valid():
            changeForm = form.save(commit=False)
            changeForm.userProfile_id = request.user.id
            changeForm.slug = request.user.username
            print(request.user.username, 33333333333333333333333333333333333333333)
            changeForm.save()
            return redirect('/')
    if request.user.is_authenticated:
        profil =  User.objects.get(pk = request.user.id).profile
        form = ProfileForm(instance=profil)
        return render(request, 'profile.html', {'form': form})

    return  HttpResponse('dont auth')