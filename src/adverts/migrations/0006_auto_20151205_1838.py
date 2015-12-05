# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0005_auto_20151203_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersProfiles',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserLogin',
        ),
        migrations.DeleteModel(
            name='UserRegistration',
        ),
    ]
