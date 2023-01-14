from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Product
from .forms import ProductModelForm
from django.urls import reverse_lazy
import json

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


class ProductCreate(UserPassesTestMixin, CreateView):
    login_url = '/login'
    form_class = ProductModelForm
    model = Product
    template_name = 'products/add_form.html'
    success_url = reverse_lazy('products')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        product = form.instance
        message = f'Produto {product.name}, cadastrado com sucesso!'

        response.headers = {
                    'HX-Trigger': json.dumps({
                        "showMessage": message
                    })}

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Repositor').exists()

class ProductUpdate(UserPassesTestMixin, UpdateView):
    login_url = '/login'
    form_class = ProductModelForm
    model = Product
    template_name = 'products/edit_form.html'
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        response = super().form_valid(form)
        product = form.instance
        message = f'Produto {product.name}, atualizado com sucesso!'

        response.headers = {
                    'HX-Trigger': json.dumps({
                        "showMessage": message
                    })}

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Repositor').exists()


class ProductDelete(UserPassesTestMixin, DeleteView):
    login_url = '/login'
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        response = super().form_valid(form)

        message = f'Produto, excluído com sucesso!'

        response.headers = {
                    'HX-Trigger': json.dumps({
                        "showMessage": message
                    })}

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Repositor').exists()
