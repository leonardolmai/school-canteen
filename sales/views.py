from django.shortcuts import render, redirect

# Create your views here.

def sales(request):
    return render(request, 'sales/sales.html')

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
