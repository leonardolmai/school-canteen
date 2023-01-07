from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from core.models import User
from django.contrib.auth.models import Group
from core.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
import json

# Create your views here.

class EmployeeCreate(UserPassesTestMixin, CreateView):
    login_url = '/login'
    form_class = UserCreationForm
    model = User
    template_name = 'employees/add_form.html'
    success_url = reverse_lazy('employees')
    
    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.instance
        group_name = self.request.POST.get('group')

        if group_name == 'Repositor':
            group = Group.objects.get(name=group_name)
            message = f'{group_name} {user.get_full_name()}, cadastrado com sucesso!'
        else:
            group = Group.objects.get(name='Vendedor')
            message = f'Vendedor {user.get_full_name()}, cadastrado com sucesso!'

        user.groups.add(group)
        user.save()
        messages.success(self.request, message)

        response.headers = {
                    'HX-Trigger': json.dumps({
                        "showMessage": message
                    })}

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists()


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


class EmployeeDetail(UserPassesTestMixin, DetailView):
    login_url = '/login'
    model = User
    template_name = 'employees/detail.html'
    queryset = User.objects.filter(groups__name__in=['Repositor', 'Vendedor'])

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists()


class EmployeeUpdate(UserPassesTestMixin, UpdateView):
    login_url = '/login'
    form_class = UserChangeForm
    model = User
    template_name = 'employees/edit_form.html'
    success_url = reverse_lazy('employees')
    queryset = User.objects.filter(groups__name__in=['Repositor', 'Vendedor'])

    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.instance
        group_name = self.request.POST.get('group')
        message = f'{user.groups.all()[0]} {user.get_full_name()}, atualizado com sucesso!'

        if group_name:
            if group_name == 'Repositor':
                group = Group.objects.get(name=group_name)
                message = f'{group_name} {user.get_full_name()}, atualizado com sucesso!'
            else:
                group = Group.objects.get(name='Vendedor')
                message = f'Vendedor {user.get_full_name()}, atualizado com sucesso!'

            user.groups.clear()
            user.groups.add(group)
        user.save()
        messages.success(self.request, message)

        response.headers = {
                    'HX-Trigger': json.dumps({
                        "showMessage": message
                    })}

        return response


    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists()


def delete_employee(request, id):
    return redirect('employees')
