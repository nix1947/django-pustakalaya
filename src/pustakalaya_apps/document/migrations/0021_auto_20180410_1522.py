# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-10 09:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0020_document_document_translator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='document.DocumentSeries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='document',
            name='license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LicenseType', verbose_name='license'),
        ),
        migrations.AlterField(
            model_name='document',
            name='submitted_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documentidentifier',
            name='identifier_id',
            field=models.CharField(blank=True, max_length=30, verbose_name='Identifier ID'),
        ),
        migrations.AlterField(
            model_name='documentlinkinfo',
            name='link_description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Link Description'),
        ),
        migrations.AlterField(
            model_name='documentlinkinfo',
            name='link_name',
            field=models.URLField(max_length=500, verbose_name='Link URL'),
        ),
    ]
