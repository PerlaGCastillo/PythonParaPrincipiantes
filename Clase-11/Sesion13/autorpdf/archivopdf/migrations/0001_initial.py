# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoPDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('archivo', models.FileField(max_length=256, upload_to='')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('tamanio', models.PositiveIntegerField(default=0)),
                ('md5sum', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=256)),
                ('sexo', models.CharField(max_length=1)),
                ('registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='archivopdf',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archivopdf.Autor'),
        ),
    ]
