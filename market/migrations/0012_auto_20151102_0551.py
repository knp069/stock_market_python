# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0011_auto_20151102_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='base_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 5, 51, 37, 995737)),
        ),
    ]
