# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150908_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manifest',
            name='manifested_waste',
        ),
        migrations.AddField(
            model_name='manifestedwaste',
            name='manifest',
            field=models.ForeignKey(default=2, to='api.Manifest'),
            preserve_default=False,
        ),
    ]
