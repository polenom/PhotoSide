from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from photojournal.models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': '123'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'123'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confim password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

class UserAuthForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': '123'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput())


class AddPhotoForm(forms.ModelForm):
    description = forms.CharField(label='Description')
    photo = forms.ImageField(label='Photo')
    class Meta:
        model = Blog
        fields = ('photo','description','title','photoPublish')

class ChangePhotoForm(forms.ModelForm):
    description = forms.CharField(label='Description')
    photo = forms.ImageField(label='Photo')
    class Meta:
        model = Blog
        fields = ('photo', 'description', 'title', 'photoPublish')



class ProfileForm(forms.ModelForm):
    dateBirthday = forms.DateField(label='Birthday', widget=forms.DateInput(attrs={'type':'date'}))
    firstName = forms.CharField(label='First name',required=False)
    secondName = forms.CharField(label='Second name', required=False)
    emailProfile = forms.EmailField(label='Email')
    userPhoto = forms.ImageField(label='Photo user' )

    class Meta:
        model = Profile
        fields = ('userPhoto', 'firstName', 'secondName', 'dateBirthday', 'emailProfile')


class CommentsForm(forms.ModelForm):
    text = forms.CharField(label='Comment')

    class Meta:
        model = Comments
        fields = ('text',)

