# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-10 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20180406_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensetype',
            name='license',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='License'),
        ),
    ]
