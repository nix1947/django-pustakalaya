# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='keyword_description',
            field=models.TextField(blank=True, default='', verbose_name='Keyword description'),
        ),
    ]
