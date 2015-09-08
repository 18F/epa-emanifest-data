# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20150908_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifestedwaste',
            name='container_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='manifestedwaste',
            name='container_type',
            field=models.CharField(max_length=5),
        ),
    ]
