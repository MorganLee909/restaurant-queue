# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-27 23:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_auto_20190725_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='line',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='seatUser',
        ),
        migrations.RemoveField(
            model_name='table',
            name='party',
        ),
    ]
