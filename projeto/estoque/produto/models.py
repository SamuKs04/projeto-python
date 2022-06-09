from django.db import models
class produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    código= models.CharField(max_length=30)
    tamanho= models.CharField(max_length=100)

def __str__():
    return self.nome
