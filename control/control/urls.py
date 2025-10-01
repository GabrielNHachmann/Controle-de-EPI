"""
URL configuration for control project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('colaboradores/', views.colaboradores, name='colaboradores'),
    path('equipamentos/', views.equipamentos, name='equipamentos'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('emprestimo/', views.emprestimo, name='emprestimo'),

    #crud
    path('criar_colaborador/', views.criar_colaborador, name='criar_colaborador'),
    path('deletar_colaborador/<int:id>', views.deletar_colaborador, name='deletar_colaborador'),
    path('deletar_equipamento/<int:id>', views.deletar_equipamento, name='deletar_equipamento'),
    path('editar_colaborador/<int:id>', views.editar_colaborador, name='editar_colaborador'),
    path('criar_equipamento/', views.criar_equipamento, name='criar_equipamento'),
    path('editar_equipamento/<int:id>', views.editar_equipamento, name='editar_equipamento'),
    path('equipamentos/<int:id>/deletar/', views.deletar_equipamento, name='deletar_equipamento'),
    path('editar_equip_status/<int:id>', views.editar_equip_status, name='editar_equip_status'),
    path('criar_emprestimo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('show_equipamento/', views.show_equipamento, name='show_equipamento'),
    path('show_emprestimos/', views.show_emprestimos, name='show_emprestimos')
]
