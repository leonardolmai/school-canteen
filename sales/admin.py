from django.contrib import admin
from .models import Sale, Product_Sale

# Register your models here.

class Product_SaleAdminInline(admin.TabularInline):
    model = Product_Sale
    fields = ('product', 'quantity',)


class SaleAdmin(admin.ModelAdmin):
    model = Sale
    ordering = ('id', 'total', 'datetime')
    list_display = ('id', 'get_client_cpf', 'payment_method', 'total', 'datetime')
    inlines = (Product_SaleAdminInline,)
    fields = ('client', 'payment_method')
    list_filter = ('payment_method', 'datetime')
    search_fields = ('client__cpf',)

    @admin.display(description='CPF cliente')
    def get_client_cpf(self, obj):
        return obj.client.cpf

admin.site.register(Sale, SaleAdmin)
