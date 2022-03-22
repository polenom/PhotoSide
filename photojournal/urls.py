from django.urls import path


from .views import *
from .models import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', basePage),
    path('register/',register, name='register' ),
    path('login/',userLogin, name='login'),
    path('logout', logoutUser, name='logout')
]





