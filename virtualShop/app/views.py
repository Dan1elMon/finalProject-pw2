from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def home(request):
    return render(request, "app/home.html")

def products_view(request):
    # Obtener todos los productos de la base de datos ordenados por ID
    products = Product.objects.all().order_by('id')

    # Obtener todas las categorías de la base de datos
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'app/products.html', context)

def product_list_view(request, gender):
    products = Product.objects.filter(gender=gender)
    context = {
        'products': products,
        'gender': gender,
    }
    return render(request, 'products_by_gender.html', context)
