# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20150908_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line_1',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_line_2',
            field=models.CharField(blank=True, null=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='generator',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='emergency_phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number 9-15 digits, entered in the format: '999999999'", regex='^\\d{9,15}$')], max_length=15),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='tracking_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='epa_id',
            field=models.CharField(max_length=12),
        ),
    ]
