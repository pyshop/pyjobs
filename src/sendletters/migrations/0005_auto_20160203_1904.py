# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendletters', '0004_auto_20160202_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionsignup',
            name='is_recruiter',
            field=models.BooleanField(verbose_name='ищу работников'),
        ),
        migrations.AlterField(
            model_name='subscriptionsignup',
            name='is_worker',
            field=models.BooleanField(verbose_name='ищу работу'),
        ),
    ]
