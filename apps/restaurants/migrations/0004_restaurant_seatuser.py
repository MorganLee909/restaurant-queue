# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-24 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_seateduser'),
        ('restaurants', '0003_auto_20190723_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='seatUser',
            field=models.ManyToManyField(related_name='seatUser', to='users.SeatedUser'),
        ),
    ]
