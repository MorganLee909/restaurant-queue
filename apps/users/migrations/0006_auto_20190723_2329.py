# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-23 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190723_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='line',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='users.LineMember'),
        ),
    ]