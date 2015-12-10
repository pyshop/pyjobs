# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0008_auto_20151209_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='key_expires',
        ),
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 12, 9)),
        ),
    ]
