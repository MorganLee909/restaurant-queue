# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-20 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantQueueApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='table',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
