from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from photojournal.models import Blog

from photojournal.models import *
# Create your views here.
from pjapi.serializer import BlogsSerializer  # , BlogUpdateSerializer


class BlogViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    # queryset = Blog.objects.all()
    serializer_class = BlogsSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk", None)
        if pk:
            return Blog.objects.filter(pk=pk)
        return Blog.objects.all()

    @action(methods=['get'], detail=False)
    def users(self,request):
        user= Profile.objects.all()
        return Response({'users':[ {i.userProfile.username : i.pk} for i in user]})

    @action(methods=['get'], detail=True)
    def user(self, request, pk=None):
        print(pk, "My Pk" )
        us = Profile.objects.get(pk = pk)
        a = us.__dict__
        return Response({'user':  {f'{k}':f'{v}' for k,v in us.__dict__.items() if '_s' not in k } })





# class BlogsAPIList(ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogsSerializer
#
#
# class BlogsAPIUpdate(UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogsSerializer
#
# class BlogAPIDel(DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogsSerializer


# class BlogsAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         try:
#             blog = User.objects.get(username=kwargs['username']).blogs.get(pk=kwargs['pk'])
#             return Response({'blog': BlogsSerializer(blog).data, 'status': 'true'})
#         except Blog.DoesNotExist as f:
#             return Response({'blog': '', 'status': 'false'})
#
#     def post(self, request):
#         try:
#             request.data['user'] = User.objects.get(username = request.data['user']).pk
#         except User.DoesNotExist:
#             return Response({'blog': '', 'result': 'false'})
#         print(request.data['user'],123333333333333)
#         serializer = BlogsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'blog':serializer.data, 'result':'true'})
#
#
#     def put(self, request):
#         slug = request.data.get('slug', None)
#
#
#         if not slug:
#             return Response({'error':"Method PUT don't allow"})
#
#         try:
#             a = Blog.objects.get(slug=slug)
#         except Blog.DoesNotExist:
#             return Response({'error':'object does not exists'})
#
#         serializer = BlogUpdateSerializer(instance=a, data=request.data)
#         print(request.data,3333333333333)
#         serializer.is_valid(raise_exception=True)
#         # if serializer.is_valid():
#         #     return Response({'blog': '', 'status': 'false'})
#         serializer.save()
#         return Response({'blog': serializer.data, 'status': 'true'})
#
#     def delete(self, request):
#         slug = request.data.get('slug', None)
#         if not slug:
#             return Response({'error':'Method DELETE not allowed'})
#         try:
#             res = Blog.objects.get(slug=slug)
#         except Blog.DoesNotExist:
#             return Response({'result': 'false'})
#         res.delete()
#         return Response({'result': 'true'})
