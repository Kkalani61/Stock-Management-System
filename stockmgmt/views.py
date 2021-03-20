from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Stock
from .forms import *
from django.contrib import messages

import csv

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect("/loginUser")
    return render(request, 'home.html')

def loginUser(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'loginUser.html')

    return render(request, 'loginUser.html')

def logoutUser(request):
    logout(request)
    return redirect("/loginUser")


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
