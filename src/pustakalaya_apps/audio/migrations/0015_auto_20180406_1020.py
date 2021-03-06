# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-06 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0014_auto_20180321_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_running_time',
            field=models.CharField(blank=True, max_length=255, verbose_name='Running time in minutes'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='type',
            field=models.CharField(default='audio', editable=False, max_length=255),
        ),
    ]
