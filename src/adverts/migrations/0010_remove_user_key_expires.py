# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0009_auto_20151209_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='key_expires',
        ),
    ]
