from django.shortcuts import render, HttpResponse, redirect
from .models import Stock
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def list_items(request):
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "title" : 'List of items',
        "queryset" : queryset,
        "form" : form
    }
    if request.method == "POST":
        queryset = Stock.objects.filter(category__icontains=form['category'].value(), item_name__icontains=form['item_name'].value())    
        context = {
        "title" : 'List of items',
        "queryset" : queryset,
        "form" : form
        }
    return render(request, "list_items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/list_items")
    context = {
        "title" : "Add Item",
        "form" : form
    }
    return render(request, "add_items.html", context)


def update_items(request, id_no):
    queryset = Stock.objects.get(id=id_no)
    form = StockUpdateForm(instance=queryset)
    if request.method == "POST":
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')
    context = {
        'form' : form
    }
    return render(request, 'add_items.html', context)


def delete_items(request, id_no):
    queryset = Stock.objects.get(id=id_no)
    if request.method == "POST":
        queryset.delete()
        return redirect("/list_items")
    return render(request, 'delete_items.html')


