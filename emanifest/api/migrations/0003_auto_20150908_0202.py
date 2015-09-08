# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150908_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generator',
            name='manifest',
        ),
        migrations.AddField(
            model_name='manifest',
            name='generator',
            field=models.ForeignKey(to='api.Generator', default=2),
            preserve_default=False,
        ),
    ]
