# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("guests", "0003_guest_is_child"),
    ]

    operations = [
        migrations.AddField(
            model_name="party",
            name="category",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
