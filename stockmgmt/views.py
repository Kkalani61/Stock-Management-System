


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
from .models import Stock, StockHistory
from .forms import *
from django.contrib import messages

import csv

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect("/base")
    return redirect('/list_items')


def base(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(request, user)
            return redirect("/list_items")
        else:
            return render(request, 'base.html')

    return render(request, 'base.html')


def logoutUser(request):
    logout(request)
    return redirect("/base")

# @login_required
def list_items(request):
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "title" : 'List of items',
        "queryset" : queryset,
        "form" : form
    }
    if request.method == "POST":
        # queryset = Stock.objects.filter(category__icontains=form['category'].value(), item_name__icontains=form['item_name'].value())    
        queryset = Stock.objects.filter(item_name__icontains=form['item_name'].value())
        if form['export_to_csv'].value() == True:
            response = HttpResponse(content_type="txt/csv")
            response['Content-Disposition'] = 'attachment; filename="Available Inventory"'
            writer = csv.writer(response)
            writer.writerow(['Category', 'Item Name', 'Quantity'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response
        context = {
        "title" : 'List of items',
        "queryset" : queryset,
        "form" : form
        }
    return render(request, "list_items.html", context)

# @login_required
def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Succesfully Added")
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
        messages.success("Succesfull deleted")
        return redirect("/list_items")
    return render(request, 'delete_items.html')


def stock_detail(request, id_no):
    queryset = Stock.objects.get(id=id_no)
    context = {
        'title' : queryset.category,
        'queryset' : queryset
    }
    return render(request, 'stock_detail.html', context)


def issue_items(request, id_no):
    queryset = Stock.objects.get(id=id_no)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity -= instance.issue_quantity
        instance.receive_quantity = 0
        instance.issue_by = str(request.user)
        messages.success(request, "Issued Successfully, " +  str(instance.quantity) +  " " +  str(instance.item_name) +  's left in stock.')
        instance.save()
        return redirect('/stock_detail/'+str(instance.id))

    context = {
        'queryset' : queryset,
        'title' : 'Issue ' + str(queryset.item_name),
        'form' : form,
        'username' : 'Issue by ' + str(request.user)
    }

    return render(request, 'add_items.html', context)


def receive_items(request, id_no):
    queryset = Stock.objects.get(id=id_no)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.quantity += instance.receive_quantity
        instance.issue_quantity = 0
        instance.receive_by = str(request.user)
        messages.success(request, "Received Successfully " + str(instance.quantity) + " " + str(instance.item_name) + "s left in stock.")
        instance.save()
        return redirect("/stock_detail/" + str(instance.id))

    context = {
        'title' : "Received " + str(queryset.item_name),
        'queryset' : queryset,
        'form' : form,
        'username' : 'Received by ' + str(request.user)
    } 
    return render(request, 'add_items.html', context)


def reorder_level(request, id_no):
    queryset = Stock.objects.get(id=id_no)
    form = ReorderForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))
        instance.save()
        return redirect("/list_items")
    context = {
        "instance" : queryset,
        "form" : form
    }

    return render(request, "add_items.html", context)


# @login_required
def list_history(request):
    header = 'LIST HISTORY'
    queryset = StockHistory.objects.all()
    form = StockHistorySearchForm(request.POST or None)
    context = {
    'title' : header,
    "queryset": queryset,
    'form' : form 
    } 
    if request.method == 'POST':
        category = form['category'].value()
        queryset = StockHistory.objects.filter(item_name__icontains=form['item_name'].value(), last_updated__range=[form['start_date'].value(), form['end_date'].value()])
        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        } 
        if (category != ''):
            queryset = queryset.filter(category_id=category)
   
        if form['export_to_csv'].value() == True:
            response = HttpResponse(content_type="txt/csv")
            response['Content-Disposition'] = 'attachment; filename="Stock History"'
            writer = csv.writer(response)
            writer.writerow(['Category', 'Item Name', 'Quantity', 'ISSUE QUANTITY', 'RECEIVE QUANTITY', 'RECEIVE QUANTITY', 'RECEIVE BY', 'ISSUE BY', 'LAST UPDATED'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity, stock.issue_quantity, stock.receive_quantity, stock.receive_by, stock.issue_by, stock.last_updated])
            return response
    context = {
        'queryset' : queryset,
        'title' : header,
        'form' : form 
    } 

    return render(request, "list_history.html", context)


def prediction(request,id):
    import pandas as pd
    import numpy as np
    from tensorflow.keras.models import load_model
    import datetime
    print('In predictions')

    with open('D:\coding\Stock-Management-System-master\stockmgmt\columns.txt', 'r') as f:
        cols_with_n = f.readlines()
        cols = list(map(lambda x: x[0: len(x)-1], cols_with_n))

    data = pd.DataFrame([0]*10325, index=cols).transpose()

    # stock = Stock()
    curr_stock = Stock.objects.get(id=id)
    print(curr_stock)
    Discount = float(request.POST['discount'])
    Shipping_Cost = float(request.POST['shippingcost'])
    date = datetime.datetime.now()+datetime.timedelta(days=1)
    print(date)
    Order_Priority = 2
    Order_Year = date.day
    Order_Month = date.month
    Order_Day = date.year
    prod_price = curr_stock.prod_price
    print(prod_price)
    Market = 'Market_EMEA'
    Product_id = 'Product ID_'+str(curr_stock.prod_id)
    Category = 'Category_'+str(curr_stock.category)
    sub_category = 'Sub-Category_'+str(curr_stock.subcategory)
    print(Category,type(Category))

    data['Discount'] = Discount
    data['Shipping Cost'] = Shipping_Cost
    data['Order Priority'] = Order_Priority
    data['OrderYear'] = Order_Year
    data['OrderMonth'] = Order_Month
    data['OrderDay'] = Order_Day
    data['prod_price'] = prod_price
    data[Market] = 1
    data[Product_id] = 1
    data[Category] = 1
    data[sub_category] = 1

    #load_model
    model = load_model(
        'D:\coding\Stock-Management-System-master\stockmgmt\SalesModel.h5')

    pred_sales = abs(model.predict(data))
    quantity = abs(pred_sales // prod_price)

    curr_stock.reorder_level=quantity
    curr_stock.save(update_fields=['reorder_level'])

    return redirect('/list_items')
