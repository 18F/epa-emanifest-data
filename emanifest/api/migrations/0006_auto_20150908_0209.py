# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150908_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manifestedwaste',
            name='instructions',
        ),
        migrations.AddField(
            model_name='manifest',
            name='special_instructions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
