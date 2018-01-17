# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='foto',
            fields=[
                ('id_foto', models.AutoField(primary_key=True, serialize=False)),
                ('nama_foto', models.CharField(max_length=120)),
                ('dokumen_foto', models.FileField(upload_to='Dokumen_foto/')),
                ('updt', models.DateTimeField(auto_now=True)),
                ('tms', models.DateTimeField(auto_now_add=True)),
                ('publish_foto', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': ' foto',
                'verbose_name': 'Detail foto',
                'ordering': ['-updt', '-tms'],
            },
        ),
    ]