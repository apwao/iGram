# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-22 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='timeline/')),
                ('image_name', models.CharField(max_length=100)),
                ('image_caption', models.TextField()),
                ('comments', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
