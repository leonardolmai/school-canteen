from django.shortcuts import render, redirect

# Create your views here.

def clients(request):
    return render(request, 'clients/clients.html')

def add_client(request):
    return redirect('clients')

def edit_client(request, id):
    return redirect('clients')

def delete_client(request, id):
    return redirect('clients')
