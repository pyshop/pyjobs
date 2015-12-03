# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0004_userlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='email',
            field=models.CharField(max_length=60, default='SOME STRING', help_text='электропочта обязательное поле', verbose_name='электропочта'),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='phone',
            field=models.CharField(max_length=60, blank=True, help_text='в любом формате', verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(max_length=60, help_text='сложный и безопасный', verbose_name='пароль'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='username',
            field=models.CharField(max_length=28, help_text='используется дла входа на сайт', verbose_name='имя пользователя'),
        ),
    ]
