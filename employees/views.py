from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from core.models import User

# Create your views here.

class EmployeeList(UserPassesTestMixin, ListView):
    login_url = '/login'
    model = User
    template_name = 'employees/employees.html'
    paginate_by = 10

    def get_queryset(self):
        employees = User.objects.filter(groups__name__in=['Repositor', 'Vendedor'])
        return employees

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists()


def add_employee(request):
    return redirect('employees')

def edit_employee(request, id):
    return redirect('employees')

def delete_employee(request, id):
    return redirect('employees')
