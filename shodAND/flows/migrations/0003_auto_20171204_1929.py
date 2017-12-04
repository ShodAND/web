# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_port_protocol'),
        ('flows', '0002_scanprocess_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanprocess',
            name='command',
        ),
        migrations.AddField(
            model_name='scanprocess',
            name='ports',
            field=models.ManyToManyField(to='base.Port'),
        ),
    ]