from django.urls import path, include
from .views import *
urlpatterns = [
    path('v1/blog/<slug:username>/<int:pk>', BlogsAPIView.as_view()),
    path('v1/blog/', BlogsAPIView.as_view()),
]