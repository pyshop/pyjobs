from django import forms
from .models import Advert, User, UserLogin


class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ('title', 'description', 'requirements', 'salary', 'city')


class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(help_text='сложный и безопасный', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'phone')


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = UserLogin
        fields = ('username', 'password')
