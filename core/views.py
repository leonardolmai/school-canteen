from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from sales.models import Sale, Product_Sale
from django.db.models.aggregates import Count, Sum
from django.contrib import messages
import datetime

# Create your views here.

class Index(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        if request.user.groups.filter(name='Gerente').exists():
            return redirect('employees')
        elif request.user.groups.filter(name='Repositor').exists():
            return redirect('products')
        elif request.user.groups.filter(name='Vendedor').exists():
            return redirect('register-sale')
        else:
            messages.warning(request, "Você não pertence a nenhum grupo")
            return redirect('login')


class Summary(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    template_name = 'core/summary.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        context['top_selling_products'] =  Product_Sale.objects.values('product__name').annotate(sold_amount=Sum('quantity')).order_by('-sold_amount')[:5]
        context['clients_who_buy_the_most'] =  Sale.objects.values('client__cpf').annotate(number_of_purchases=Count('client')).order_by('-number_of_purchases')[:5]
        context['almost_expired_products'] = Product.objects.order_by('validity')[:5]
        context['products_with_low_stock'] = Product.objects.order_by('quantity')[:5]

        current_date = datetime.date.today()
        context['today_sales'] = Sale.objects.filter(datetime__day=current_date.day).aggregate(Count('id'), Sum('total'))
        context['yesterday_sales'] = Sale.objects.filter(datetime__day=current_date.day-1).aggregate(Count('id'), Sum('total'))
        context['week_sales'] = Sale.objects.filter(datetime__week=current_date.isocalendar()[1]).aggregate(Count('id'), Sum('total'))
        context['month_sales'] = Sale.objects.filter(datetime__month=current_date.month).aggregate(Count('id'), Sum('total'))

        return context
