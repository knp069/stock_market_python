from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class company(models.Model):
    name = models.CharField(max_length=30)
    base_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0,)
    profit_loss = models.SmallIntegerField(default=0)
    percentage = models.FloatField(default=0)
    def __unicode__(self):
        return self.name


class owner(models.Model):
    user = models.ForeignKey(User)
    gender = models.SmallIntegerField(default=0)
    phone_number = models.CharField(max_length=20,null=True)
    company = models.ForeignKey(company)
    def __unicode__(self):
        return self.user.username

class broker(models.Model):
    user = models.ForeignKey(User)
    gender = models.SmallIntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    def __unicode__(self):
        return self.user.username


class stock_holder(models.Model):
    user = models.ForeignKey(User)
    gender = models.SmallIntegerField()
    phone = models.CharField(max_length=20)
    hard_asset = models.FloatField(default=100000)
    soft_asset = models.FloatField(default=0)
    total_asset = models.FloatField(default=0)
    profit_loss = models.SmallIntegerField(default=0)
    def __unicode__(self):
        return self.user.username

class news(models.Model):
    news_id = models.IntegerField()
    news = models.CharField(max_length=300)
    state = models.SmallIntegerField(default=0)
    def __unicode__(self):
        return self.news

class newsEffect(models.Model):
    news = models.ForeignKey(news)
    company = models.ForeignKey(company)
    profitOrLoss = models.SmallIntegerField(default=0)
    percentage = models.FloatField(default=0)
    def __unicode__(self):
        return self.news.news

class transaction(models.Model):
    broker_id = models.ForeignKey(broker)
    user = models.ForeignKey(stock_holder)
    company = models.ForeignKey(company)
    num_shares = models.IntegerField()
    cost_per_share = models.FloatField()
    buy_sell = models.SmallIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now())
    def __unicode__(self):
        return str(self.transaction_id)


class stockowner(models.Model):
    owner = models.ForeignKey(stock_holder)
    stock_owned  = models.ForeignKey(company)
    number_of_stock = models.IntegerField(default=0)