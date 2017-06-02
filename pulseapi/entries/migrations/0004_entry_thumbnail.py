# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-16 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import pulseapi.entries.models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20170220_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=2048, upload_to=pulseapi.entries.models.entry_thumbnail_path),
        ),
    ]