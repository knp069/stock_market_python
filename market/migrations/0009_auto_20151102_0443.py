# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20151102_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_holder',
            name='total_asset',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 4, 43, 46, 182612)),
        ),
    ]
