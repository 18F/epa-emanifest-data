# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20150923_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifestedwaste',
            name='dot_packing_group',
            field=models.CharField(blank=True, default='', max_length=6, null=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III')]),
        ),
    ]
