# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-06 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20180306_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='publication_year_on_text',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Publication year'),
        ),
        migrations.AlterField(
            model_name='video',
            name='year_of_available',
            field=models.DateField(blank=True, null=True, verbose_name='Year of available on text'),
        ),
        migrations.AlterField(
            model_name='video',
            name='year_of_available_on_text',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Year of available'),
        ),
    ]