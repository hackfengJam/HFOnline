# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-16 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_auto_20170916_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_tell',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='you_need_know',
        ),
    ]
