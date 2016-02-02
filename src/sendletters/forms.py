from django import forms

from .models import SubscriptionSignUp


class SubscriptionSignUpForm(forms.ModelForm):
    class Meta:
        model = SubscriptionSignUp
        fields = ['email', 'full_name', 'is_worker', 'is_recruiter']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label='Имя')
    email = forms.EmailField(max_length=120, label='Электропочта')
    subject = forms.CharField(max_length=120, label='Тема')
    message = forms.CharField(max_length=1000, label='Сообщение', widget=forms.Textarea)
