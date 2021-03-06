# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-20 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_genre_audio_video'),
        ('audio', '0018_auto_20180413_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='audio_genre',
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_genre',
            field=models.ManyToManyField(blank=True, to='core.genre_audio_video', verbose_name='Audio Genre'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='audio_original_document_authors',
            field=models.ManyToManyField(blank=True, related_name='audio_original_document_authors', to='core.Biography', verbose_name='Original Author(s)'),
        ),
    ]
