from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

def user_path(instance, filename):
    return f'static/Profile/Photo/%Y/%m/%d/username_{instance.userProfile}_id_{instance.userProfile.id}_{datetime.now()}.jpg'

def photo_path(instance, filename):
    date = datetime.now()
    return f'static/images/{date.year}/{date.month}/{date.day}/date_{date.hour}-{date.minute}-{date.minute}'

class Profile(models.Model):
    userProfile = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='')
    userPhoto = models.FileField(upload_to=user_path,blank=True,default='', verbose_name='Фото')
    firstName = models.TextField(max_length=30,blank=True,default='', verbose_name='Имя')
    secondName = models.TextField(max_length=30,blank=True,default='', verbose_name='Фамилия')
    dateBirthday = models.DateTimeField(blank=True, null=True, verbose_name='День рождения')
    emailProfile = models.EmailField(max_length=200, verbose_name='Почта')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'

class Subcription(models.Model):
    subscriber = models.ForeignKey(Profile,on_delete=models.CASCADE)
    sub = models.ForeignKey(User, on_delete=models.PROTECT)

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    photo = models.ImageField(upload_to=photo_path, verbose_name='Фото')
    description = models.TextField(max_length=100, verbose_name='Описание')
    creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    photoPublish = models.BooleanField(default=True, verbose_name='Статус')

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Фото')
    text = models.TextField(max_length=100, verbose_name='Коментарий')
    creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')


