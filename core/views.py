from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return redirect('employees')

def summary(request):
    return render(request, 'core/summary.html')
