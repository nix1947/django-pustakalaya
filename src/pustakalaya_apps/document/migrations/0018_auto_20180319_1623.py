# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-19 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180314_1648'),
        ('document', '0017_auto_20180313_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_illustrators',
            field=models.ManyToManyField(blank=True, related_name='illustrators', to='core.Biography', verbose_name='Illustrator'),
        ),
        migrations.RemoveField(
            model_name='document',
            name='publisher',
        ),
        migrations.AddField(
            model_name='document',
            name='publisher',
            field=models.ManyToManyField(blank=True, null=True, related_name='publisher', to='core.Publisher', verbose_name='Publisher name'),
        ),
    ]
