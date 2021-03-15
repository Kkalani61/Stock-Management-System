from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("list_items/", views.list_items, name="list_tems"),
    path("add_items/", views.add_items, name="add_items")
]