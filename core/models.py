from mailbox import NotEmptyError
from django.db import models

# Create your models here.
class Camisas(models.Model):
    tamanho = models.CharField("Tamanho", max_length=2)
    marca = models.CharField("Marca do produto", max_length=100)
    tipo = models.CharField("Tipo", max_length=100)
    nome = models.CharField("Nome", max_length=100)
    ano = models.CharField("Ano de lançamento", max_length=4)
    personalizacao = models.IntegerField("Númeração da Camisa")
    foto = models.FileField("Foto do Produto")

class Short(models.Model):
    modelo = models.CharField("Modelo", max_length=100)
    tamanho = models.CharField("Tamanho", max_length=2)
    marca = models.CharField("Marca", max_length=100)
    tipo = models.CharField("Tipo", max_length=100)
    foto = models.FileField("Foto do Produto")
    

class Calcados(models.Model):
    modelo = models.CharField("Modelo", max_length=100)
    tamanho = models.CharField("Tamanho", max_length=2)
    marca = models.CharField("Marca", max_length=100)
    tipo = models.CharField("Tipo", max_length=100)
    foto = models.FileField("Foto do Produto")

