# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-30 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20150814_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='rotation_required',
            field=models.BooleanField(default=False),
        ),
    ]