# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_useractivationkey_password_recovery_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_recruiter',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_worker',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
