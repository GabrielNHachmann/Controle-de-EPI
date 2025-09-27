from django import forms
from app.models import Equipamento
from app.models import Emprestimo


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'tipo', 'codigo', 'estoque']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome aqui'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o tipo aqui'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o código aqui'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade em estoque'}),
        }

