from django.shortcuts import render, redirect

# Create your views here.

def sales(request):
    return render(request, 'sales/sales.html')

def day_report(request):
  return redirect('sales')

def week_report(request):
  return redirect('sales')

def month_report(request):
  return redirect('sales')
