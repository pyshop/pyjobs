# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20160220_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email_to_contact',
            field=models.EmailField(blank=True, default=None, help_text='может отличаться от указанной при регистрации', max_length=120, null=True, verbose_name='электропочта для связи'),
        ),
    ]
