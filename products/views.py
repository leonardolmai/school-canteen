from django.shortcuts import render, redirect

# Create your views here.

def products(request):
    return render(request, 'products/products.html')

def add_product(request):
    return redirect('products')

def edit_product(request, id):
    return redirect('products')

def delete_product(request, id):
    return redirect('products')
