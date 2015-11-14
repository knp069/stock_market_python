# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_auto_20151102_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='state',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 6, 59, 16, 152909)),
        ),
    ]
