from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Product

# Create your views here.

class ProductList(UserPassesTestMixin, ListView):
    login_url = '/login'
    model = Product
    template_name = 'products/products.html'
    paginate_by = 10

    def get_queryset(self):
        products = Product.objects.all()
        return products

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Repositor').exists() or self.request.user.groups.filter(name='Vendedor').exists() 


class ProductDetail(UserPassesTestMixin, DetailView):
    login_url = '/login'
    model = Product
    template_name = 'products/detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Repositor').exists()


def add_product(request):
    return redirect('products')

def edit_product(request, id):
    return redirect('products')

def delete_product(request, id):
    return redirect('products')
