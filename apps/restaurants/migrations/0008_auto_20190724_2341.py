# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-24 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20190724_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='party',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table', to='users.SeatedUser'),
        ),
    ]
