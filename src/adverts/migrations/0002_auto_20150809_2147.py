# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'verbose_name_plural': 'вакансии', 'verbose_name': 'вакансия'},
        ),
        migrations.AddField(
            model_name='advert',
            name='city',
            field=models.CharField(help_text='название города', default='', max_length=50, verbose_name='город'),
        ),
        migrations.AddField(
            model_name='advert',
            name='requirements',
            field=models.TextField(blank=True, verbose_name='требования к соискателю'),
        ),
        migrations.AddField(
            model_name='advert',
            name='salary',
            field=models.CharField(help_text='до пятидесяти символов', default='', max_length=50, verbose_name='зарплата'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='author',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='автор вакансии'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание вакансии'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='title',
            field=models.CharField(help_text='краткое описание отражающее суть вакансии', max_length=127, verbose_name='название вакансии'),
        ),
    ]
