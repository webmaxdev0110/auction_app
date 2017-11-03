# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20171102_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.CharField(choices=[('shipping', 'Shipping'), ('returning', 'Returning'), ('arrived', 'Arrived'), ('cancelled', 'Cancelled')], default='shipping', max_length=50),
        ),
    ]
