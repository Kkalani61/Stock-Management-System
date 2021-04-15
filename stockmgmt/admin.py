from django.contrib import admin
from .models import *
from .forms import StockCreateForm


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['item_name','prod_id','category','subcategory', 'quantity', 'prod_price']
    form  = StockCreateForm
    list_filter = ['category', 'item_name']
    search_fields = ['category', 'item_name']
    


# Register your models here.
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(StockHistory)
# admin.site.register(Product)
# admin.site.register(StockCreateForm)
# admin.site.register(StockCreateAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)
