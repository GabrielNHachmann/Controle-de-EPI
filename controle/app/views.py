from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'app/pages/base.html')

def colaboradores(request):
    return render(request, 'app/pages/colaboradores.html')

def equipamentos(request):
    return render(request, 'app/pages/equipamentos.html')