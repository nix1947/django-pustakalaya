# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('abstract', models.TextField(blank=True, verbose_name='Abstract/Summary')),
                ('additional_note', models.TextField(blank=True, verbose_name='Additional Note')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('license_type', models.CharField(choices=[('creative commons', 'Creative commons'), ('copyright retained', 'Copyright retained'), ('apache License 2.0', 'Apache license 2.0'), ('creative commons', 'Creative commons'), ('mit license', 'मानोज'), ('custom license', 'Custom License'), ('na', 'Not available')], max_length=255, verbose_name='License type')),
                ('custom_license', models.TextField(blank=True, verbose_name='Rights')),
                ('year_of_available', models.DateField(blank=True, null=True, verbose_name='Year of available')),
                ('publication_year', models.DateField(blank=True, null=True, verbose_name='Publication year')),
                ('place_of_publication', models.CharField(blank=True, max_length=255, verbose_name='Place of publication')),
                ('volume', models.CharField(blank=True, default='', max_length=254)),
                ('edition', models.CharField(blank=True, default='', max_length=254)),
                ('document_type', models.CharField(choices=[('book', 'Book'), ('working paper', 'Working paper'), ('thesis', 'Thesis'), ('journal paper', 'Journal paper'), ('technical report', 'Technical report'), ('article', 'Article')], max_length=40, verbose_name='Document type')),
                ('document_file_type', models.CharField(choices=[('ppt', 'PPT'), ('doc', 'Doc'), ('docx', 'Docx'), ('pdf', 'PDF'), ('pdf', 'PDF'), ('xlsx', 'Excel'), ('epub', 'Epub'), ('rtf', 'Rtf'), ('mobi', 'Mobi')], max_length=23, verbose_name='Document file type')),
                ('document_interactivity', models.CharField(choices=[('yes', 'हो'), ('no', 'होइन'), ('NA', 'Not applicable')], max_length=15, verbose_name='Interactive')),
                ('type', models.CharField(default='document', editable=False, max_length=255)),
                ('document_total_page', models.PositiveIntegerField(blank=True, verbose_name='Total Pages')),
                ('document_thumbnail', models.ImageField(max_length=255, upload_to='uploads/thumbnails/audio/%Y/%m/%d')),
                ('collections', models.ManyToManyField(to='collection.Collection', verbose_name='Add to these collections')),
                ('document_authors', models.ManyToManyField(blank=True, related_name='authors', to='core.Biography', verbose_name='Author(s)')),
                ('document_editors', models.ManyToManyField(blank=True, related_name='editors', to='core.Biography', verbose_name='Editor(s)')),
                ('document_illustrators', models.ManyToManyField(blank=True, related_name='illustrators', to='core.Biography', verbose_name='Document Illustrator')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='DocumentFileUpload',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('file_name', models.CharField(max_length=255, verbose_name='File name')),
                ('upload', models.FileField(max_length=255, upload_to='uploads/documents/%Y/%m/')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.Document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('identifier_type', models.CharField(choices=[('issn', 'ISSN'), ('ismn', 'ISMN'), ('govt_doc', "Gov't Doc"), ('uri', 'URI'), ('isbn', 'ISBN')], max_length=8, verbose_name='Identifier Type')),
                ('identifier_id', models.CharField(blank=True, max_length=10, verbose_name='Identifier ID')),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='document.Document', verbose_name='document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentLinkInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('link_name', models.URLField(verbose_name='Link URL')),
                ('link_description', models.CharField(max_length=500, verbose_name='Link Description')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.Document', verbose_name='Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentSeries',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('series_name', models.CharField(max_length=255, verbose_name='Series name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='document_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.DocumentSeries', verbose_name='Series'),
        ),
        migrations.AddField(
            model_name='document',
            name='education_levels',
            field=models.ManyToManyField(blank=True, to='core.EducationLevel', verbose_name='Education Levels'),
        ),
        migrations.AddField(
            model_name='document',
            name='keywords',
            field=models.ManyToManyField(to='core.Keyword', verbose_name='Select list of keywords'),
        ),
        migrations.AddField(
            model_name='document',
            name='languages',
            field=models.ManyToManyField(to='core.Language', verbose_name='Language(s)'),
        ),
        migrations.AddField(
            model_name='document',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Publisher', verbose_name='Publisher name'),
        ),
        migrations.AddField(
            model_name='document',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='core.Sponsor', verbose_name='Sponsor'),
        ),
    ]