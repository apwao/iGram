# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='editor',
            field=models.IntegerField(default=0),
        ),
    ]
