from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField('primeiro nome', max_length=32)
    last_name = models.CharField('último nome', max_length=32)
    phone = models.CharField('telefone', max_length=14)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('e-mail', unique=True)

    def __str__(self):
        return self.email
