# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-13 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='creator',
        ),
    ]
