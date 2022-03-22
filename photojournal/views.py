from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import UserRegisterForm, UserAuthForm
from .models import *


def basePage(request):
    form = UserAuthForm()
    param = {'tasks': Blog.objects.all(),
             'form': form}

    return render(request,'base.html',param)


def register(request):
    if request.method == 'POST':
        userReg = UserRegisterForm(request.POST)
        if userReg.is_valid():
            userReg.save()
            user= User.objects.get(username = request.POST['username'])
            Profile(userProfile=user, emailProfile= request.POST['email']).save()
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

class BlogView(ListView):
    model = Blog
    template_name = 'base.html'
    context_object_name = 'tasks'

    def get_gueryset(self):
        return  Blog.objects.all()


class Login(LoginView):
    template_name = 'base.html'
    redirect_field_name = '/'