# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20151102_0310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='no of available stocks',
            new_name='available_stock',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 3, 47, 10, 207194)),
        ),
    ]
