import io
import datetime
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Sale, Product_Sale
from products.models import Product
from django.db.models.aggregates import Count, Sum
from clients.models import Client
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import FileResponse
from reportlab.pdfgen import canvas

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

            for name, quantity in products_sold.items():
                product = Product.objects.get(name=name)
                if product.quantity < int(quantity):
                    messages.error(request, f'Quantidade não disponível de {product.name}, tem {product.quantity} em estoque para venda.')
                    return redirect(self.success_url)

            sale.save()

            for name, quantity in products_sold.items():
                product = Product.objects.get(name=name)
                product.quantity = product.quantity - int(quantity)
                product.save()
                product_sale = Product_Sale(sale=sale, product=product, quantity=quantity, price=product.price)
                product_sale.save()

            messages.success(request, 'Venda registrada com sucesso!')
    
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(quantity__gte=1)
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists()


class DayReport(UserPassesTestMixin, View):
    login_url = '/login'
   
    def get(self, request):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)

        current_date = datetime.date.today()

        pdf.setTitle(f'day-report-{current_date}')
        pdf.setFont('Helvetica-Oblique', 14)
        pdf.drawString(220, 820, f'Relatório do dia {current_date.strftime("%d/%m/%Y")}')
       
        payment_method = Sale.objects.filter(datetime__day=current_date.day).values('payment_method').annotate(count=Count('payment_method')).order_by('-count').first()
        pdf.setFont('Helvetica', 12)
        if payment_method != None:
            pdf.drawString(10, 790, f'Método de pagamento mais utilizado: {payment_method["payment_method"]}, em {payment_method["count"]} vendas.')

        sold_amount = sum([product.quantity for product in Product_Sale.objects.filter(sale__datetime__day=current_date.day)])
        pdf.drawString(10, 770, f'Foram vendidos: {sold_amount} produtos.')

        total_sales_value = Sale.objects.filter(datetime__day=current_date.day).aggregate(Count('id'), Sum('total'))
        pdf.drawString(10, 750, f'Valor total de vendas: R${total_sales_value["total__sum"]:.2f}')

        y = 720
        pdf.setFont('Helvetica-Bold', 10)
        pdf.drawString(10, y, 'ID')
        pdf.drawString(60, y, 'CPF cliente')
        pdf.drawString(160, y, 'Método de pagamento')
        pdf.drawString(280, y, 'Total')
        pdf.drawString(380, y, 'Data e hora')
        pdf.line(10, y-5, 585, y-5)
        y = y - 20

        for sale in Sale.objects.filter(datetime__day=current_date.day):
            if y <= 40:
                pdf.showPage()
                y = 790
            pdf.setFont('Helvetica', 10)
            pdf.drawString(10, y, f'{sale}')
            pdf.drawString(60, y, f'{sale.client.cpf}')
            pdf.drawString(160, y, f'{sale.payment_method}')
            pdf.drawString(280, y, f'R${sale.total:.2f}')
            pdf.drawString(380, y, f'{sale.datetime.strftime("%d/%m/%Y às %H:%M")}')
            pdf.line(10, y-5, 585, y-5)
            y = y - 20

        pdf.showPage()
        pdf.save()

        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename=f'day-report-{current_date}.pdf')

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists()


class WeekReport(UserPassesTestMixin, View):
    login_url = '/login'

    def get(self, request):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)

        current_date = datetime.date.today()

        pdf.setTitle(f'week-report-{current_date.isocalendar()[1]}-{current_date.year}')
        pdf.setFont('Helvetica-Oblique', 14)
        pdf.drawString(220, 820, f'Relatório da semana {current_date.isocalendar()[1]} de {current_date.year}')
       
        payment_method = Sale.objects.filter(datetime__week=current_date.isocalendar()[1]).values('payment_method').annotate(count=Count('payment_method')).order_by('-count').first()
        pdf.setFont('Helvetica', 12)
        if payment_method != None:
            pdf.drawString(10, 790, f'Método de pagamento mais utilizado: {payment_method["payment_method"]}, em {payment_method["count"]} vendas.')

        sold_amount = sum([product.quantity for product in Product_Sale.objects.filter(sale__datetime__week=current_date.isocalendar()[1])])
        pdf.drawString(10, 770, f'Foram vendidos: {sold_amount} produtos.')

        total_sales_value = Sale.objects.filter(datetime__week=current_date.isocalendar()[1]).aggregate(Count('id'), Sum('total'))
        pdf.drawString(10, 750, f'Valor total de vendas: R${total_sales_value["total__sum"]:.2f}')

        y = 720
        pdf.setFont('Helvetica-Bold', 10)
        pdf.drawString(10, y, 'ID')
        pdf.drawString(60, y, 'CPF cliente')
        pdf.drawString(160, y, 'Método de pagamento')
        pdf.drawString(280, y, 'Total')
        pdf.drawString(380, y, 'Data e hora')
        pdf.line(10, y-5, 585, y-5)
        y = y - 20

        for sale in Sale.objects.filter(datetime__week=current_date.isocalendar()[1]):
            if y <= 40:
                pdf.showPage()
                y = 790
            pdf.setFont('Helvetica', 10)
            pdf.drawString(10, y, f'{sale}')
            pdf.drawString(60, y, f'{sale.client.cpf}')
            pdf.drawString(160, y, f'{sale.payment_method}')
            pdf.drawString(280, y, f'R${sale.total:.2f}')
            pdf.drawString(380, y, f'{sale.datetime.strftime("%d/%m/%Y às %H:%M")}')
            pdf.line(10, y-5, 585, y-5)
            y = y - 20

        pdf.showPage()
        pdf.save()

        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename=f'week-report-{current_date.isocalendar()[1]}-{current_date.year}.pdf')

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists()

def month_report(request):
    return redirect('sales')
