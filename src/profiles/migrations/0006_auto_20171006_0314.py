# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 03:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20171006_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
