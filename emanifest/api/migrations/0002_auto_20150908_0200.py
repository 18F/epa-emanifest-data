# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manifest',
            name='generator',
        ),
        migrations.AddField(
            model_name='generator',
            name='manifest',
            field=models.ForeignKey(default=2, to='api.Manifest'),
            preserve_default=False,
        ),
    ]
