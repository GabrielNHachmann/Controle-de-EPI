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
    estoque = models.IntegerField()
    status = models.CharField(max_length=100, default='Novo') 


def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    colaborador = models.ForeignKey(
        Colaborador,
        on_delete=models.CASCADE # Outras opções comuns: models.PROTECT, models.SET_NULL
    )

    equipamento = models.ForeignKey(
        Equipamento,
        on_delete=models.CASCADE
    )

    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

def __str__(self):
        return f"Empréstimo de {self.equipamento.nome} para {self.colaborador.nome}"
        