from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=False)
    nome_completo = models.CharField(
        max_length=255, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    telefone = models.CharField(max_length=22, verbose_name='Telefone')

    def __str__(self):
        return f'{self.nome_completo} - {self.email}'
