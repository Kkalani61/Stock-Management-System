from django import forms
from .models import Stock, StockHistory
from bootstrap_datepicker_plus import DatePickerInput

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item_name', 'prod_id', 'category',
                  'subcategory', 'quantity', 'prod_price']

class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name']
    export_to_csv = forms.BooleanField(required=False)

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category", 'item_name', "quantity"]


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['prod_price', 'issue_quantity', 'discount', 'sales', 'shipMode', 'shipping_cost', 'order_priority']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity',]


class ReorderForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level', ]
        

class StockHistorySearchForm(forms.ModelForm):
    export_to_csv = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta: 
        model = StockHistory
        fields = ['category', 'item_name', 'start_date', 'end_date']
