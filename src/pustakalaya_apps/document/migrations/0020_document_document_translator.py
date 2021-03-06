# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-03 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20180320_1424'),
        ('document', '0019_auto_20180319_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_translator',
            field=models.ManyToManyField(blank=True, related_name='translators', to='core.Biography', verbose_name='Translator(s)'),
        ),
    ]
