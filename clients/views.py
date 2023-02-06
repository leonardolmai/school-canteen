from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from .models import Client
from .forms import ClientModelForm
from django.urls import reverse_lazy
import json

# Create your views here.

class ClientList(UserPassesTestMixin, ListView):
    login_url = '/login'
    model = Client
    template_name = 'clients/clients.html'
    paginate_by = 10

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        search = self.request.GET.get('search')

        if sort and search:
            clients = Client.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(email__icontains=search) | Q(cpf__icontains=search) | Q(phone__icontains=search)).order_by(sort)
        elif sort:
            clients = Client.objects.order_by(sort)
        elif search:
            clients = Client.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(email__icontains=search) | Q(cpf__icontains=search) | Q(phone__icontains=search))
        else:
            clients = Client.objects.all()

        return clients

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists() 


class ClientDetail(UserPassesTestMixin, DetailView):
    login_url = '/login'
    model = Client
    template_name = 'clients/detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists() 


class ClientCreate(UserPassesTestMixin, CreateView):
    login_url = '/login'
    form_class = ClientModelForm
    model = Client
    template_name = 'clients/add_form.html'
    success_url = reverse_lazy('clients')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        client = form.instance
        message = f'Cliente {client.first_name}, cadastrado com sucesso!'

        response.headers = {
                    'HX-Trigger': json.dumps({
                        "showMessage": message
                    })}

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists() 


class ClientUpdate(UserPassesTestMixin, UpdateView):
    login_url = '/login'
    form_class = ClientModelForm
    model = Client
    template_name = 'clients/edit_form.html'
    success_url = reverse_lazy('clients')

    def form_valid(self, form):
        response = super().form_valid(form)
        client = form.instance
        message = f'Cliente {client.first_name}, atualizado com sucesso!'

        response.headers = {
                    'HX-Trigger': json.dumps({
                        "showMessage": message
                    })}

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists() 


class ClientDelete(UserPassesTestMixin, DeleteView):
    login_url = '/login'
    model = Client
    template_name = 'clients/delete.html'
    success_url = reverse_lazy('clients')

    def form_valid(self, form):
        response = super().form_valid(form)

        message = f'Cliente, excluído com sucesso!'

        response.headers = {
                    'HX-Trigger': json.dumps({
                        "showMessage": message
                    })}

        return response
    
    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists() or self.request.user.groups.filter(name='Vendedor').exists() 
