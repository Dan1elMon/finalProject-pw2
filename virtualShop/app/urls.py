from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category" ),

]
