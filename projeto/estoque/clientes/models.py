from django.db import models
class clientes(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13)
    login = models.CharField(max_length=100)

def __str__(self):
    return self.nome
