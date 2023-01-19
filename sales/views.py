from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Sale

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

def register_sale(request):
    if request.method == 'GET':
      return render(request, 'sales/register-sale.html')
    elif request.method == 'POST':
      return redirect('register-sale')

def day_report(request):
    return redirect('sales')

def week_report(request):
    return redirect('sales')

def month_report(request):
    return redirect('sales')
