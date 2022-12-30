from django.shortcuts import render, redirect

# Create your views here.

def summary(request):
    return render(request, 'core/summary.html')
