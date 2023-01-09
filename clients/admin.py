from django.contrib import admin
from .models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    model = Client
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'cpf', 'phone')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Client, ClientAdmin)
