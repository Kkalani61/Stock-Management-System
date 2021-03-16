from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("list_items/", views.list_items, name="list_tems"),
    path("add_items/", views.add_items, name="add_items"),
    path('update_items/<str:id_no>/', views.update_items, name="update_items"),
    path('delete_items/<str:id_no>/', views.delete_items, name="delete_items")
]