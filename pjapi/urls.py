from django.urls import path, include
from .views import *
urlpatterns = [
    path('v1/blog/', BlogViewSet.as_view({'get':'list', 'post':'create'})),
    path('v1/blog/<int:pk>', BlogViewSet.as_view({'put':'update', 'delete':'destroy'}))
]