# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20151101_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broker',
            name='broker_id',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 2, 25, 13, 60441)),
        ),
    ]
