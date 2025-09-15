from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento
from .models import Colaborador
from .form import EquipamentoForm


# Create your views here.
def home(request):
    return render(request, 'app/pages/home.html')

def colaboradores(request):
    return render(request, 'app/pages/colaboradores.html')

def equipamentos(request):
    return render(request, 'app/pages/equipamentos.html')


def criar_colaborador(request):
    if request.method == 'GET':
        colaboradores = Colaborador.objects.all()
        return render(request, 'app/pages/colaboradores.html', {'colaboradores': colaboradores})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        status = request.POST.get('status') == '1'
        funcao = request.POST.get('funcao')

        colaborador = Colaborador(
            nome=nome,
            email=email,
            telefone=telefone,
            status=status,
            funcao=funcao
        )  

        colaborador.save() 

        return redirect('criar_colaborador')

def editar_colaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)

    if request.method == 'GET':
        return render(request, 'app/pages/colaboradores.html', {'colaborador': colaborador})
    elif request.method == 'POST':
        colaborador.nome = request.POST.get('nome')
        colaborador.email = request.POST.get('email')
        colaborador.telefone = request.POST.get('telefone')
        colaborador.status = request.POST.get('status') == '1'
        colaborador.funcao = request.POST.get('funcao')

        colaborador.save() 

        return redirect('criar_colaborador')
    
def deletar_colaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)
    colaborador.delete()
    return redirect('criar_colaborador')


#parte do equipamento
def criar_equipamento(request):
    equipamentos = Equipamento.objects.all()

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criar_equipamento')
    else:
        form = EquipamentoForm()

    return render(request, 'app/pages/equipamentos.html', {
        'form': form,
        'equipamentos': equipamentos
    })

def editar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)

    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('criar_equipamento')
    else:
        form = EquipamentoForm(instance=equipamento)

    return render(request, 'app/pages/equipamentos.html', {
        'form': form,
        'equipamento': equipamento
    })

def deletar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.delete()
    return redirect('criar_equipamento')

