# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-25 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from pulseapi.entries.models import ModerationState, Entry

def forwards_func(apps, schema_editor):
    approved = ModerationState.objects.get(name='Approved')
    entries = apps.get_model('entries', 'Entry').objects.all()
    for entry in entries:
        if entry.is_approved:
            migrated_entry = Entry.objects.get(
                title=entry.title,
                content_url=entry.content_url
            )
            migrated_entry.moderation_state = approved
            migrated_entry.save()


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0009_entry_moderation_state'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]