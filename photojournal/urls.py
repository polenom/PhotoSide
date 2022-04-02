from django.urls import path
from .views import *



urlpatterns = [
    path('', basePage),
    path('register/',register, name='register' ),
    path('login/',userLogin, name='login'),
    path('logout', logoutUser, name='logout'),
    path('add', addPhoto, name='add'),
    path('blog/<slug:slug>', viewBlog, name= 'blog'),
    path('profile/<slug:slug>', viewProfile, name='profile'),
    path('blogs/<slug:slug>', viewBlogs, name='blogs'),
    path('sub/<int:pk>', subUser, name='subuser'),
    path('like/<slug:slug>', likeBlog, name='like')
]





