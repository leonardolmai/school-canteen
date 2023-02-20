from django.db import models
from clients.models import Client
from products.models import Product
from django.core.validators import MinValueValidator

# Create your models here.

class Sale(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Cartão de crédito', 'Cartão de crédito'),
        ('Cartão de débito', 'Cartão de débito'),
        ('Dinheiro', 'Dinheiro'),
        ('PIX', 'PIX'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_method = models.CharField('método de pagamento', choices=PAYMENT_METHOD_CHOICES, max_length=20)
    total = models.FloatField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='Product_Sale')

    def __str__(self):
        return f'{self.id}'


class Product_Sale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField('preço', validators=[MinValueValidator(0.0)])
    quantity = models.PositiveIntegerField('quantidade')

    class Meta:
        unique_together = [['sale', 'product']]

    def __str__(self):
        return f'{self.id}'
    
    def get_total(self):
        return self.price * self.quantity
