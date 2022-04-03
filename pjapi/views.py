from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from  photojournal.models import Blog

from photojournal.models import *
# Create your views here.
from pjapi.serializer import BlogsSerializer


class BlogsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            blog = User.objects.get(username=kwargs['username']).blogs.get(pk=kwargs['pk'])
            return Response({'blog': BlogsSerializer(blog).data, 'status': 'true'})
        except Blog.DoesNotExist as f:
            return Response({'blog': '', 'status': 'false'})

    def post(self, request):
        try:
            request.data['user'] = User.objects.get(username = request.data['user']).pk
        except User.DoesNotExist:
            return Response({'blog': '', 'result': 'false'})
        serializer = BlogsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'blog':serializer.data, 'result':'true'})



