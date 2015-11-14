# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20151102_0347'),
    ]

    operations = [
        migrations.CreateModel(
            name='stockowner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_stock', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(to='market.stock_holder')),
                ('stock_owned', models.ForeignKey(to='market.company')),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 4, 26, 2, 597453)),
        ),
    ]
