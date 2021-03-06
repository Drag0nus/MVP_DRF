# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-25 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170413_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='weather',
            field=models.CharField(default='', help_text='Info about current weather, when user info has been updated', max_length=300),
        ),
    ]
