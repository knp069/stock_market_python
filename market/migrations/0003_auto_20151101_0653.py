# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20151101_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='profit_loss',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newseffect',
            name='profitOrLoss',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock_holder',
            name='profit_loss',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 6, 53, 53, 677420)),
        ),
    ]
