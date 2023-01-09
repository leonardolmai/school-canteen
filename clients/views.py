from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Client

# Create your views here.

class ClientList(UserPassesTestMixin, ListView):
    login_url = '/login'
    model = Client
    template_name = 'clients/clients.html'
    paginate_by = 10

    def get_queryset(self):
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


def add_client(request):
    return redirect('clients')

def edit_client(request, id):
    return redirect('clients')

def delete_client(request, id):
    return redirect('clients')
