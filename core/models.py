from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField('e-mail', unique=True)
    phone = models.CharField('telefone', max_length=14)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    photo = models.ImageField('foto', upload_to='profile', default='user.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'cpf']

    def __str__(self):
        return self.username
