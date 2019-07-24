# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-23 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190723_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('partySize', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='users.LineMember'),
        ),
    ]
