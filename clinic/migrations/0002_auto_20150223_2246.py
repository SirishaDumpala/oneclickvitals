# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient_name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_first_name',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_last_name',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
    ]
