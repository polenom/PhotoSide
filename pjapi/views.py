from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from  photojournal.models import Blog

from photojournal.models import *
# Create your views here.
from pjapi.serializer import BlogsSerializer, BlogUpdateSerializer


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
        print(request.data['user'],123333333333333)
        serializer = BlogsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'blog':serializer.data, 'result':'true'})


    def put(self, request):
        slug = request.data.get('slug', None)


        if not slug:
            return Response({'error':"Method PUT don't allow"})

        try:
            a = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            return Response({'error':'object does not exists'})

        serializer = BlogUpdateSerializer(instance=a, data=request.data)
        print(request.data,3333333333333)
        serializer.is_valid(raise_exception=True)
        # if serializer.is_valid():
        #     return Response({'blog': '', 'status': 'false'})
        serializer.save()
        return Response({'blog': serializer.data, 'status': 'true'})

    def delete(self, request):
        slug = request.data.get('slug', None)
        if not slug:
            return Response({'error':'Method DELETE not allowed'})
        try:
            res = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            return Response({'result': 'false'})
        res.delete()
        return Response({'result': 'true'})