# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_auto_20150223_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient_phone_number',
            field=models.CharField(null=True, max_length=10),
            preserve_default=True,
        ),
    ]
