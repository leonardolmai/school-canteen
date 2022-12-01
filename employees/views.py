from django.shortcuts import render, redirect

# Create your views here.

def employees(request):
    return render(request, 'employees/employees.html')

def add_employee(request):
    return redirect('employees')

def edit_employee(request, id):
    return redirect('employees')

def delete_employee(request, id):
    return redirect('employees')
