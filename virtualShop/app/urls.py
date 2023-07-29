from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('products/', views.products_view, name='products'),

    path('products/male/', views.product_list_view, {'gender': 'Male'}, name='male_products'),
    path('products/female/', views.product_list_view, {'gender': 'Female'}, name='female_products'),
    path('products/unisex/', views.product_list_view, {'gender': 'Unisex'}, name='unisex_products'),
]
