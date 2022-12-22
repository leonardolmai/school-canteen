from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request, 'core/login.html')

def logout(request):
    return redirect('login')

def summary(request):
    return render(request, 'core/summary.html')
