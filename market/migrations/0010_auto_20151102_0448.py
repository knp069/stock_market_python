# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20151102_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_id',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 4, 48, 12, 967693)),
        ),
    ]
