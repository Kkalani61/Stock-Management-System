from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

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
        fields = ['issue_quantity', 'issue_by']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity',]

