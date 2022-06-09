from django.db import models
class Nota_fiscal(models.Model):
    nomeProd = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=6)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13)
    CNPJ = models.CharField(max_length=100)

def __str__(self):
    return self.nome
