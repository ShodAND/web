# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20171119_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='privileged',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
