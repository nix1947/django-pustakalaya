# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-25 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0024_auto_20180510_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='videofileupload',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='maximum size of thumbnail should be 165px by 93px', max_length=255, null=True, upload_to='uploads/thumbnails/videofile/%Y/%m/%d'),
        ),
    ]
