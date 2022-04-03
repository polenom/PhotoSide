from django.shortcuts import render
from rest_framework import generics
from photojournal.models import *
# Create your views here.
from pjapi.serializer import BlogsSerializer


class BlogsAPIView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-creation')
    serializer_class = BlogsSerializer