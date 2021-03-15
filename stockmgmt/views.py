from django.shortcuts import render, HttpResponse, redirect
from .models import Stock
from .forms import StockCreateForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def list_items(request):
    title = 'List of items',
    queryset = Stock.objects.all()
    context = {
        "title" : title,
        "queryset" : queryset
    }
    return render(request, "list_items.html", context)

def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/list_items")
    context = {
        "form" : form,
        "title" : "Add Item"
    }
    return render(request, "add_items.html", context)