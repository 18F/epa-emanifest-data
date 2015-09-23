# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20150923_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='epaentity',
            name='certification_statments',
            field=models.TextField(blank=True, default='I hereby declare that the contents         of this consignment are fully and         accurately described above by the proper shipping name, and are         classified, packaged, marked and labeled/placarded, and are in all         respects in proper condition for transport according to applicable         international and national governmental regulations. If export         shipment and I am the Primary Exporter, I certify that the         contents of this consignment conform to the terms of the         attached EPA Acknowledgment of Consent. I certify that the waste         minimization statement identified in 40 CFR 262.27(a) (if I am a         large quantity generator) or (b) (if I am a small quantity         generator) is true.', null=True),
        ),
        migrations.AddField(
            model_name='epaentity',
            name='signature',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='epaentity',
            name='signature_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='epaentity',
            name='signature_name',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
    ]
