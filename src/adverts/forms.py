from django import forms
from .models import Advert, User, UserActivationKey


class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ('title', 'description', 'requirements', 'salary', 'city')


class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(help_text='еще раз', widget=forms.PasswordInput(), label='Password',)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']

    def if_password_didnt_match(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.is_active = False
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class EditUserProfileForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=30, required=False)
    last_name = forms.CharField(label='last name', max_length=30, required=False)
    email = forms.CharField(label='mail', max_length=30, required=False)
    phone = forms.CharField(label='phone', max_length=30, required=False)
