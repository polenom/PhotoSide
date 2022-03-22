from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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
