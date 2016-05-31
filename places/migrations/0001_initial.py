# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to=stdimage.utils.UploadToUUID(path='places'), verbose_name='Image')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
