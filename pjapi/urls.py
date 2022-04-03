from django.urls import path, include
from .views import *
urlpatterns = [
    path('v1/blogs', BlogsAPIView.as_view()),
]