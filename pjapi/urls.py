from django.urls import path, include
from .views import *
urlpatterns = [
    path('v1/blog/', BlogsAPIList.as_view()),
    path('v1/blog/<int:pk>', BlogsAPIUpdate.as_view()),
    path('v1/blog/del/<int:pk>',BlogAPIDel.as_view())
]