
from django.contrib import admin
from .models import Product

##admin.site.register(Product)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','discounted_price','category','product_image']