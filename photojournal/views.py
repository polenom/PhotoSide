from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import UserRegisterForm, UserAuthForm, AddPhotoForm, ProfileForm, CommentsForm
from .models import *
from django.db.models import Q, Count


def basePage(request):
    form = UserAuthForm()
    if request.user.is_authenticated:
        print(request.user)
        user = User.objects.get(username = request.user)
        us = user.profile
        blogs = Blog.objects.filter(Q(photoPublish=True)& ~Q(user=request.user.id)).order_by('-creation')
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
                venue.slug = request.POST['title']
                venue.save()
                return redirect('/')
        else:
            form = AddPhotoForm()
        return render(request,'add.html', {'form':form})


def viewBlog(request, slug):
    reqid = Blog.objects.get(slug=slug).user
    form = CommentsForm()
    if request.user.is_authenticated and request.user == reqid:
        blog = User.objects.get(pk = request.user.id).blogs.get(slug=slug)
        comments = blog.coms.all().order_by('-creation')
        if request.method == 'POST':
            form = CommentsForm(request.POST)
            if form.is_valid():
                value = form.save(commit=False)
                value.user = User.objects.get(pk =request.user.id)
                value.blog = blog
                value.save()
                form = CommentsForm()
        return render(request,'blog.html', {'blog':blog,'username':User.objects.get(pk = request.user.id).username, 'comments': comments,'form':form, 'delete': True })
    elif request.user.is_authenticated:
        blog =Blog.objects.get(slug=slug)
        comments = blog.coms.all().order_by('-creation')
        if request.method == 'POST':
            form = CommentsForm(request.POST)
            if form.is_valid():
                value = form.save(commit=False)
                value.user = User.objects.get(pk =request.user.id)
                value.blog = blog
                value.save()
                form = CommentsForm()
        # if request.method == "POST":
        #     suber = Profile.objects.get(user=request.user.id)
        #     suber =
        return render(request, 'blog.html', {'blog': blog,'username':blog.user.username, 'comments': comments,'form':form, 'delete': False})
    return HttpResponse('Ok')


def viewProfile(request, slug):
    if request.method == 'POST' and request.user.is_authenticated:
        user = User.objects.get(pk = request.user.id).profile
        form = ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    if request.user.is_authenticated:
        profil =  User.objects.get(pk = request.user.id).profile
        form = ProfileForm(instance=profil)
        return render(request, 'profile.html', {'form': form})

    return  HttpResponse('dont auth')


def viewBlogs(request, slug):
    reqid = User.objects.get(username=slug).pk
    print(reqid,111111111111111111111111111111111)
    if request.user.is_authenticated and request.user.id == reqid:
        user = User.objects.get(username=request.user)
        us = user.profile
        blogs = user.blogs.all().order_by('-creation')
        subcount = Profile.objects.exclude(pk = request.user.id).filter(sub=request.user.id).aggregate(Count('sub'))['sub__count']
        return render(request, 'myblogs.html', {'us': us, 'blogs':blogs,'subcount':subcount})
    elif request.user.is_authenticated and request.user.id != reqid:
        us = User.objects.get(pk=reqid)
        blogs = Blog.objects.filter(Q(photoPublish=True)&Q(user=reqid)).order_by('-creation')
        subcount = Profile.objects.exclude(pk=reqid).filter(sub=reqid).aggregate(Count('sub'))['sub__count']
        sub = False
        if Profile.objects.get(pk=request.user.id).sub.filter(pk=reqid):
            sub=True
        return render(request, 'blogsotheruser.html', {'us': us, 'blogs': blogs, 'sub':sub,'subcount': subcount})
    return HttpResponse('ошибка 404')


def subUser(request, pk):
    try:
        user=User.objects.get(pk=pk)
        suber = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        user = False

    if user and suber:
        print(suber.username)
        check = suber.profile.sub.filter(pk = pk)

        if check:
            suber.profile.sub.remove(user)
        else:
            suber.profile.sub.add(user)
    return redirect(f'/blogs/{user.profile.slug}')


def likeBlog(request, slug):
    try:
        blog  = Blog.objects.get(slug=slug)
        like = User.objects.get(pk = request.user.id)
    except User.DoesNotExist or Blog.DoesNotExist:
        like = False
    if blog and like:
        check = blog.likesBlog.filter(pk=request.user.id)
        if check:
            blog.likesBlog.remove(like)
        else:
            blog.likesBlog.add(like)
    return redirect(f'/blog/{slug}')

def removeBlog(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return HttpResponse('404')
    if request.user.is_authenticated and blog.user == request.user:
        blog.delete()
    return redirect('/')