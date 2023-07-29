from django.http import HttpResponse
from django.shortcuts import render, Category

# Create your views here.

def home(request):
    return render(request, "app/home.html")

def products_view(request):
    # Obtener todos los productos de la base de datos
    products = Product.objects.all()

    # Obtener todas las categorías de la base de datos
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products.html', context)