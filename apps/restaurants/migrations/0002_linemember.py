# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-23 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('partySize', models.IntegerField()),
                ('restaurant', models.ManyToManyField(related_name='line', to='restaurants.Restaurant')),
            ],
        ),
    ]
