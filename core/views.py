from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

class Index(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        if request.user.groups.filter(name='Gerente').exists():
            return redirect('employees')
        elif request.user.groups.filter(name='Repositor').exists():
            return redirect('products')
        elif request.user.groups.filter(name='Vendedor').exists():
            return redirect('register-sale')
        else:
            messages.warning(request, "Você não pertence a nenhum grupo")
            return redirect('login')


def summary(request):
    return render(request, 'core/summary.html')
