# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20171119_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='label',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
    ]
