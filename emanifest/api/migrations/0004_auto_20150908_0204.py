# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150908_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manifest',
            name='transporter',
        ),
        migrations.AddField(
            model_name='transporter',
            name='manifest',
            field=models.ForeignKey(to='api.Manifest', default=2),
            preserve_default=False,
        ),
    ]
