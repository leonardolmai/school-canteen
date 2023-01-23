from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Sale, Product_Sale
from products.models import Product
from clients.models import Client
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class SaleList(UserPassesTestMixin, ListView):
    login_url = '/login'
    model = Sale
    template_name = 'sales/sales.html'
    paginate_by = 10

    def get_queryset(self):
        sales = Sale.objects.all()
        return sales
    
    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists()


class SaleDetail(UserPassesTestMixin, DetailView):
    login_url = '/login'
    model = Sale
    template_name = 'sales/detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists()


class RegisterSale(UserPassesTestMixin, CreateView):
    login_url = '/login'
    model = Sale
    template_name = 'sales/register-sale.html'
    fields = '__all__'
    success_url = reverse_lazy('register-sale')

    def post(self, request):
        products_sold = dict(zip(request.POST.getlist('products'), request.POST.getlist('quantities')))
        cpf = request.POST.get('client-cpf')
        if not Client.objects.filter(cpf=cpf).exists():
            messages.error(request, f'Cliente não cadastrado, faça o cadastro do cliente com o CPF {cpf}, e tente novamente.')
        elif len(products_sold) == 0:
            messages.error(request, 'Nenhum produto adicionado, adicione pelo menos um.')
        else:
            client = Client.objects.get(cpf=cpf)
            payment_method = request.POST.get('payment-method')
            sale = Sale(client=client, payment_method=payment_method)
            sale.save()

            for name, quantity in products_sold.items():
                product = Product.objects.get(name=name)
                product_sale = Product_Sale(sale=sale, product=product, quantity=quantity)
                product_sale.save()

            messages.success(request, 'Venda registrada com sucesso!')
    
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists()


def day_report(request):
    return redirect('sales')

def week_report(request):
    return redirect('sales')

def month_report(request):
    return redirect('sales')
