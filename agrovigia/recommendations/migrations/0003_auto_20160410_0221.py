# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_auto_20160410_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='max_temp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='min_temp',
            field=models.FloatField(),
        ),
    ]
