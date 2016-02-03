from django.db import models

# Create your models here.


class SubscriptionSignUp(models.Model):
    class Meta:
        verbose_name = "подписка на рассылку"
        verbose_name_plural = "подписки на рассылку"
    # предполагается, что подписка доступна без создания пользователя
    email = models.EmailField(max_length=120, blank=False, null=True, verbose_name='электропочта')
    full_name = models.CharField(max_length=120, blank=False, null=True, default='', verbose_name='имя')
    is_worker = models.BooleanField(verbose_name='ищу работу')
    is_recruiter = models.BooleanField(verbose_name='ищу работников')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
