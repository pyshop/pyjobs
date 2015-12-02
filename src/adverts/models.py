from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

from django_extensions.db.models import TimeStampedModel


class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    phone = models.CharField('номер телефона', max_length=127, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return 'user-detail', (self.pk,)

    def __str__(self):
        name = self.get_full_name()
        if not name:
            name = self.username
        return name


class Advert(TimeStampedModel):
    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    title = models.CharField(verbose_name='название вакансии', max_length=127, blank=False,
                             help_text='краткое описание отражающее суть вакансии')
    description = models.TextField(verbose_name='описание вакансии', blank=True)
    requirements = models.TextField(verbose_name='требования к соискателю', blank=True)
    salary = models.CharField(verbose_name='зарплата', max_length=50, blank=False,
                             help_text='до пятидесяти символов', default='')
    city = models.CharField(verbose_name='город', max_length=50, blank=False,
                            help_text='название города', default='')
    author = models.ForeignKey(User, verbose_name='автор вакансии', blank=True, null=True)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'advert-detail', (self.pk,)


class UserRegistration(models.Model):
    username = models.CharField(blank=False, max_length=28,
                                verbose_name='имя пользователя', help_text='используется дла входа на сайт')
    password1 = models.CharField(blank=False, max_length=60,
                                verbose_name='пароль', help_text='сложный и безопасный')
    password2 = models.CharField(blank=False, max_length=60, verbose_name='пароль еще раз', help_text='пароль еще раз для проверки')
    email = models.CharField(blank=False, max_length=60, verbose_name='электропочта', help_text='электропочта обязательное поле')
    phone = models.CharField(blank=True, max_length=60, verbose_name='телефон', help_text='в любом формате')

    def __str__(self):
        return self.title

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserRegistration, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLogin(models.Model):
    username = models.CharField(blank=False, max_length=28, help_text='имя пользователя')
    password = models.CharField(blank=False, max_length=60, help_text='пароль')

    def __str__(self):
        return self.title