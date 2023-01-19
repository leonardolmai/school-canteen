from django.apps import AppConfig
from django.db.models import signals
from .signals import product_sale_post_save

class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'

    def ready(self): 
        from .models import Sale

        signals.post_save.connect(product_sale_post_save, sender=Sale.products.through)
