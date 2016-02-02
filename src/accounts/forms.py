from django import forms

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120, label='юзернейм')
    # email = forms.EmailField(label='электропочта')
    password = forms.CharField(widget=forms.PasswordInput, label='пароль')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120, label='юзернейм')
    email = forms.EmailField(label='электропочта')
    password = forms.CharField(widget=forms.PasswordInput, label='пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='пароль еще раз')
    '''
    https://docs.djangoproject.com/en/1.9/ref/forms/validation/#form-field-default-cleaning
    '''
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Юзернейм %s уже используется" % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Электропочта %s уже используется" % email)
        return email

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data
