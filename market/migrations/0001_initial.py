# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='broker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('broker_id', models.IntegerField()),
                ('gender', models.SmallIntegerField(default=0)),
                ('phone_number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('no of available stocks', models.IntegerField(default=0)),
                ('profit_loss', models.BinaryField(default=True)),
                ('percentage', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_id', models.IntegerField()),
                ('news', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='newsEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profitOrLoss', models.BinaryField(default=True)),
                ('percentage', models.FloatField(default=0)),
                ('company', models.ForeignKey(to='market.company')),
                ('news', models.ForeignKey(to='market.news')),
            ],
        ),
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.SmallIntegerField(default=0)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('company', models.ForeignKey(to='market.company')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='stock_holder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.SmallIntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('hard_asset', models.FloatField(default=100000)),
                ('soft_asset', models.FloatField(default=0)),
                ('profit_loss', models.BinaryField(default=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.IntegerField(null=True)),
                ('num_shares', models.IntegerField()),
                ('cost_per_share', models.FloatField()),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 11, 1, 6, 34, 26, 273969))),
                ('broker_id', models.ForeignKey(to='market.broker')),
                ('company', models.ForeignKey(to='market.company')),
                ('user', models.ForeignKey(to='market.stock_holder')),
            ],
        ),
    ]
