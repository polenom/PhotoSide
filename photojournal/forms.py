from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from modeltranslation.forms import TranslationModelForm
from photojournal.models import *
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput(attrs={'class': '123'}))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class':'123'}))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput())
    password2 = forms.CharField(label=_('Confim password'), widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

class UserAuthForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput(attrs={'class': '123'}))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput())


class AddPhotoForm(forms.ModelForm):
    description = forms.CharField(label=_('Description'))
    photo = forms.ImageField(label=_('Photo user'))
    class Meta:
        model = Blog
        fields = ('photo','description','title','photoPublish')

class ChangePhotoForm(forms.ModelForm):
    description = forms.CharField(label=_('Description'))
    photo = forms.ImageField(label=_('Photo'))
    class Meta:
        model = Blog
        fields = ('photo', 'description', 'title', 'photoPublish')



class ProfileForm(forms.ModelForm):
    dateBirthday = forms.DateField(label=_('Birthday'), widget=forms.DateInput(attrs={'type':'date'}, format=('%Y-%m-%d')))
    firstName = forms.CharField(label=_('First name'),required=False)
    secondName = forms.CharField(label=_('Second name'), required=False)
    emailProfile = forms.EmailField(label=_('Email'))
    userPhoto = forms.ImageField(label=_('Photo user'))

    class Meta:
        model = Profile
        fields = ('userPhoto', 'firstName', 'secondName', 'dateBirthday', 'emailProfile')


class CommentsForm(forms.ModelForm):
    # text = forms.CharField(label='Comment')

    class Meta:
        model = Comments
        fields = ('text',)

