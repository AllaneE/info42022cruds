from mailbox import NotEmptyError
from django.db import models

# Create your models here.
class Camisas(models.Model):
    tamanho = models.CharField()
    marca = models.CharField()
    tipo = models.CharField()
    nome = models.CharField()
    ano = models.DateField()
    pernosalizacao = models.IntegerField("numero")