# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 12:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 4, 17, 12, 54, 43, 537329, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
