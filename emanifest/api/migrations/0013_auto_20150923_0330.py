# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20150922_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='EPAEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('epa_id', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12, blank=True, null=True)),
                ('address', models.ForeignKey(blank=True, to='api.Address', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='desinatedfacility',
            name='address',
        ),
        migrations.RenameField(
            model_name='manifestedwaste',
            old_name='description',
            new_name='dot_description',
        ),
        migrations.RemoveField(
            model_name='transporter',
            name='epa_id',
        ),
        migrations.RemoveField(
            model_name='transporter',
            name='name',
        ),
        migrations.AddField(
            model_name='manifestedwaste',
            name='dot_hazard_class',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manifestedwaste',
            name='dot_id',
            field=models.CharField(max_length=6, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manifestedwaste',
            name='dot_packing_group',
            field=models.CharField(max_length=6, blank=True, choices=[('Any of', 'Any of'), ('I', 'I'), ('II', 'II'), ('III', 'III')], null=True),
        ),
        migrations.AddField(
            model_name='manifestedwaste',
            name='dot_shipping_name',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='designated_facility',
            field=models.ForeignKey(to='api.EPAEntity'),
        ),
        migrations.DeleteModel(
            name='DesinatedFacility',
        ),
        migrations.AddField(
            model_name='transporter',
            name='transporter',
            field=models.ForeignKey(to='api.EPAEntity', default=''),
            preserve_default=False,
        ),
    ]
