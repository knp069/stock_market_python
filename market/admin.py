from django.contrib import admin
import models
# Register your models here.



class stockownerdisplay(admin.ModelAdmin):
    list_display = ('owner','stock_owned','number_of_stock')

class transactiondisplay(admin.ModelAdmin):
    list_display = ('broker_id','user','company','num_shares','cost_per_share','time')

class companydisplay(admin.ModelAdmin):
    list_display = ('name','price','quantity','available_stock','profit_loss','percentage')

class stock_holderdisplay(admin.ModelAdmin):
    list_display = ('user','hard_asset','soft_asset','total_asset','phone','gender')


admin.site.register(models.company,companydisplay)
admin.site.register(models.stock_holder,stock_holderdisplay)
admin.site.register(models.owner)
admin.site.register(models.transaction,transactiondisplay)
admin.site.register(models.news)
admin.site.register(models.broker)
admin.site.register(models.stockowner , stockownerdisplay)
admin.site.register(models.newsEffect)