# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_generator_transporter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manifestedwaste',
            name='containers',
        ),
        migrations.AddField(
            model_name='manifestedwaste',
            name='container_quantity',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='manifestedwaste',
            name='container_type',
            field=models.CharField(default='DM', max_length=5),
        ),
        migrations.DeleteModel(
            name='Container',
        ),
    ]
