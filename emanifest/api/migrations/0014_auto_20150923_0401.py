# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20150923_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifestedwaste',
            name='container_type',
            field=models.CharField(max_length=2, choices=[('BA', 'Burlap, cloth, paper, or plastic bags'), ('CF', 'Fiber or plastic boxes, cartons, cases'), ('CM', 'Metal boxes, cartons, cases (including roll-offs'), ('CW', 'Wooden boxes, cartons, cases'), ('CY', 'Cylinders'), ('DF', 'Fiberboard or plastic drums, barrels, kegs'), ('DM', 'Metal drums, barrels, kegs'), ('DW', 'Wooden drums, barrels, kegs'), ('HG', 'Hopper or gondola cars'), ('TC', 'Tank cars'), ('TP', 'Portable tanks'), ('TT', 'Cargo tanks (tank trucks).')]),
        ),
        migrations.AlterField(
            model_name='manifestedwaste',
            name='dot_packing_group',
            field=models.CharField(max_length=6, blank=True, null=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III')]),
        ),
        migrations.AlterField(
            model_name='manifestedwaste',
            name='units_of_measure',
            field=models.CharField(max_length=1, choices=[('G', 'Gallons (liquids only)'), ('N', 'Cubic Meters'), ('K', 'Kilograms P = Pounds'), ('L', 'Liters (liquids only)'), ('T', 'Tons (2000 Pounds)'), ('M', 'Metric Tons (1000 Kilograms)'), ('Y', 'Cubic Yards')]),
        ),
    ]
