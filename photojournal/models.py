from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

def user_path(instance, filename):
    date = datetime.now()
    return f'static/Photo/{date.year}/{date.month}/{date.day}/username_{instance.userProfile}_id_{instance.userProfile.id}_{datetime.now()}.{filename.split(".")[1]}'

def photo_path(instance, filename):
    date = datetime.now()
    return f'static/images/{date.year}/{date.month}/{date.day}/date_{date.hour}-{date.minute}-{date.minute}.{filename.split(".")[1]}'

class Profile(models.Model):
    userProfile = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='',related_name='profile',primary_key=True)
    userPhoto = models.FileField(upload_to=user_path,blank=True,default='', verbose_name='Фото',null=True)
    firstName = models.CharField(max_length=30,blank=True,default='', verbose_name='Имя',null=True)
    secondName = models.CharField(max_length=30,blank=True,default='', verbose_name='Фамилия', null=True)
    dateBirthday = models.DateTimeField(blank=True, null=True, verbose_name='День рождения')
    emailProfile = models.EmailField(max_length=200, verbose_name='Почта',null=True)
    sub=models.ManyToManyField(User,related_name='sub', blank=True)
    slug = models.SlugField(null=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'



class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя',related_name='blogs')
    photo = models.ImageField(upload_to=photo_path, verbose_name=_('Photo'))
    description = models.TextField(max_length=100, verbose_name=_('Description'))
    creation = models.DateTimeField(auto_now=True, verbose_name=_('Date create'))
    photoPublish = models.BooleanField(default=True, verbose_name=_('Status'))
    likesBlog = models.ManyToManyField(User,blank=True, related_name='likes')
    title = models.CharField(max_length=40, unique=True,verbose_name=_('Title'))
    slug = models.SlugField(null=True)

    def  __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Фото', related_name='coms')
    text = models.TextField(max_length=100, verbose_name=_('text'))
    creation = models.DateTimeField(auto_now=True, verbose_name=_('date create'))




