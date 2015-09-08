# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=3)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(default='US', max_length=100, choices=[('US', 'United States'), ('MX', 'Mexico'), ('PR', 'Puerto Rico')])),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('number', models.IntegerField()),
                ('container_type', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DesinatedFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('epa_id', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.ForeignKey(to='api.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('mailing_and_address_same', models.BooleanField()),
                ('address', models.ForeignKey(to='api.Address')),
                ('mailing_address', models.ForeignKey(blank=True, related_name='mailing_address', to='api.Address', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='International',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('import_to_us', models.BooleanField()),
                ('export_from_us', models.BooleanField()),
                ('port', models.CharField(max_length=200)),
                ('date_at_port', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('emergency_phone', models.CharField(max_length=15)),
                ('tracking_number', models.CharField(max_length=200)),
                ('number_of_pages', models.IntegerField()),
                ('designated_facility', models.ForeignKey(to='api.DesinatedFacility')),
                ('generator', models.ForeignKey(to='api.Generator')),
                ('international', models.ForeignKey(blank=True, to='api.International', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManifestedWaste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('hazardous_waste', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
                ('total_quantity', models.IntegerField()),
                ('units_of_measure', models.CharField(max_length=5)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('containers', models.ForeignKey(to='api.Container')),
            ],
        ),
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('epa_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WasteCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('code_type', models.CharField(max_length=3, choices=[('F', 'Federal'), ('S', 'State')])),
            ],
        ),
        migrations.AddField(
            model_name='manifestedwaste',
            name='waste_codes',
            field=models.ForeignKey(blank=True, to='api.WasteCode', null=True),
        ),
        migrations.AddField(
            model_name='manifest',
            name='manifested_waste',
            field=models.ForeignKey(to='api.ManifestedWaste'),
        ),
        migrations.AddField(
            model_name='manifest',
            name='transporter',
            field=models.ForeignKey(to='api.Transporter'),
        ),
        migrations.AddField(
            model_name='generator',
            name='transporter',
            field=models.ManyToManyField(to='api.Transporter'),
        ),
    ]
