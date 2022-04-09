from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet, basename='blog')
print(router.urls)






urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth-sid/', include('rest_framework.urls')),
    path('v1/token/', GetToken.as_view())
    # path('v1/blog/', BlogViewSet.as_view({'get':'list', 'post':'create'})),
    # path('v1/blog/<int:pk>', BlogViewSet.as_view({'put':'update', 'delete':'destroy'}))
]