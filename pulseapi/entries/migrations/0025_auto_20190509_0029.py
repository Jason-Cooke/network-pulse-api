# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-09 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0024_entry_entry_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content_url',
            field=models.URLField(blank=True),
        ),
    ]