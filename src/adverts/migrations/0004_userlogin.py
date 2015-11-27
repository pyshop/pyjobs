# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0003_userregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=28, help_text='имя пользователя')),
                ('password', models.CharField(max_length=60, help_text='пароль')),
            ],
        ),
    ]
