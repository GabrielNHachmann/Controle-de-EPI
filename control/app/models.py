from django.db import models

# Create your models here.
class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(default=True) 
    funcao = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return self.nome
    
class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)
    estoque = models.IntegerField()

    def _str_(self):
        return self.nome