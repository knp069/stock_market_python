__author__ = 'nishant'


from celery import task
from models import *
import random import *



@task()
def updateStock():
    company_list = []
    company_list = company.objects.all()
    for companies in company_list:
        rint = randint(0,1)
        if rint == 0:
            companies.price = companies.price-companies.price*percent
            companies.percentage = (companies.price-companies.base_price)*100/companies.base_price
            if companies.percentage < 0 :
                companies.profit_loss=0
            else :
                companies.profit_loss=1
        else:
            companies.price = companies.price+companies.price*percent
            companies.percentage = (companies.price-companies.base_price)*100/companies.base_price
            if companies.percentage < 0 :
                companies.profit_loss=0
            else :
                companies.profit_loss=1
        companies.save()
