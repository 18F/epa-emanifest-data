# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20150908_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastecode',
            name='code_type',
            field=models.CharField(max_length=10, choices=[('Federal', 'Federal'), ('State', 'State')]),
        ),
    ]
