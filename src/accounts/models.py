from django.db import models

from django.contrib.auth.models import AbstractUser

from pyjobs2 import settings
# Create your models here.


class User(AbstractUser):
    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    location = models.CharField(max_length=120, verbose_name='город', blank=True, null=True, default='')
    phone = models.CharField(verbose_name='номер телефона', max_length=120, blank=True, default='', null=True)
    is_worker = models.BooleanField(verbose_name='ищу работу', default=False)
    is_recruiter = models.BooleanField(verbose_name='ищу работников', default=False)
    homepage = models.URLField(verbose_name='персональный сайт', default='', blank=True, null=True)
    email_to_contact = models.EmailField(verbose_name='электропочта для связи',
                                         help_text='может отличаться от указанной при регистрации',
                                         max_length=120, default='', blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)


class UserActivationKey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    activation_key = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.user.username
