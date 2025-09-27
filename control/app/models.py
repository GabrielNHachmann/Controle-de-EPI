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

class Emprestimo(models.Model):
    nome = models.ForeignKey(Colaborador,
        on_delete=models.SET_NULL, 
        null=True,                 
        blank=True,                
        related_name='colaborador_emprestados'
    )
    nome = models.ForeignKey(Equipamento,
        on_delete=models.SET_NULL, 
        null=True,                 
        blank=True,                
    related_name='equipamentos_emprestados'
    )
    status = models.ForeignKey(Equipamento,
        on_delete=models.SET_NULL, 
        null=True,                 
        blank=True,                
    related_name='status_emprestados'
    )

def __str__(self):
        return f"{self.nome} ({self.colaborador.nome if self.colaborador else 'Disponível'})"

        