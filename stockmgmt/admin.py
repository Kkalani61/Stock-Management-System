from django.contrib import admin
from .models import Stock
from .forms import StockCreateForm

# Register your models here.
admin.site.register(Stock)
