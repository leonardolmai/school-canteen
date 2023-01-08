from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    ordering = ('name', 'price', 'quantity', 'validity')
    list_display = ('name', 'price', 'quantity', 'validity', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)
