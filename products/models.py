from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Product(models.Model):
    PRODUCT_CATEGORY_CHOICES = [
        ('Salgado', 'Salgado'),
        ('Doce', 'Doce'),
        ('Bebida', 'Bebida'),
        ('Especial', 'Especial'),
        ('Outros', 'Outros'),
    ]

    name = models.CharField('nome', max_length=32, unique=True)
    price = models.FloatField('preço', validators=[MinValueValidator(0.0)])
    quantity = models.PositiveIntegerField('quantidade')
    validity = models.DateField('validade')
    category = models.CharField('categoria', choices=PRODUCT_CATEGORY_CHOICES, max_length=20, blank=True, null=True)
    description = models.TextField('descrição', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
