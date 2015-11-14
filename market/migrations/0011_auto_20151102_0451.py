# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_auto_20151102_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='buy_sell',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 4, 51, 34, 193298)),
        ),
    ]
