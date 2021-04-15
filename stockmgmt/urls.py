from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path("/", views.home, name="index"),
    path('', views.base, name="login"),
    path('logoutUser/', views.logoutUser, name="logout"),
    # path('accounts/', include('registration.backends.default.urls')),
    path("list_items/", views.list_items, name="list_tems"),
    path("add_items/", views.add_items, name="add_items"),
    path('update_items/<str:id_no>/', views.update_items, name="update_items"),
    path('delete_items/<str:id_no>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:id_no>/', views.stock_detail, name="stock_detail"),
    path('issue_items/<str:id_no>/', views.issue_items, name="issue_items"),
    path('receive_items/<str:id_no>/', views.receive_items, name="receive_items"),
    path('reorder_level/<str:id_no>/', views.reorder_level, name="reorder_level"),
    path('list_history/', views.list_history, name="list_history"),
    path('reorder_product/<int:id>/',views.prediction),
]  