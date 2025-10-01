from django import forms
from app.models import Equipamento, Emprestimo



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


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'equipamento', 'data_devolucao'] 
        widgets = {
            'colaborador': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o colaborador'}),
            'equipamento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o equipamento'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Digite a data de devolução'})
        }