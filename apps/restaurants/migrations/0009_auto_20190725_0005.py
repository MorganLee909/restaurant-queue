# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-25 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20190724_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='party',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table', to='users.SeatedUser'),
        ),
    ]