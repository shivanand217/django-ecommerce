# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-17 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190317_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='abc'),
        ),
    ]
