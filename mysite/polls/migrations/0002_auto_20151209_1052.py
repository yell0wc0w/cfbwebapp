# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=1),
        ),
    ]
