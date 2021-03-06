# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-20 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20180410_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='genre_audio_video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('custom_genre', models.CharField(max_length=255, unique=True, verbose_name='Keyword')),
                ('genre_description', models.TextField(blank=True, default='', verbose_name='Keyword description')),
            ],
            options={
                'db_table': 'custom_genre',
            },
        ),
    ]
