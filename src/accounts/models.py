from django.db import models

from django.contrib.auth.models import AbstractUser

from pyjobs2 import settings
# Create your models here.


class User(AbstractUser):
    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    phone = models.CharField(verbose_name='номер телефона', max_length=120, blank=True)
    is_worker = models.BooleanField(verbose_name='Ищу работу', default=False)
    is_recruiter = models.BooleanField(verbose_name='Ищу работников', default=False)


class UserActivationKey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    activation_key = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.user.username
