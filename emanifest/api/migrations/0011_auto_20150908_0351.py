# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150908_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifest',
            name='special_instructions',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
