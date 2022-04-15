from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from photojournal.models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': '123'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'123'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтвердить пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

class UserAuthForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': '123'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('photo','description','title','photoPublish')

class ChangePhotoForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('photo', 'description', 'title', 'photoPublish')



class ProfileForm(forms.ModelForm):
    dateBirthday = forms.DateField(label='День рождения', widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = Profile
        fields = ('userPhoto', 'firstName', 'secondName', 'dateBirthday', 'emailProfile')


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)

