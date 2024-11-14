from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def pedidos(request):
    form = FormServicos.objects.all()
    return render(request, 'pedidos.html', context = {'form': form})

def cadastrar(request):
    if request.method == 'POST':
        form = formulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pedidos')
    else:

        form = formulario()
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)
    
def administrador(request):
    pendentes = FormServicos.objects.filter(aceita=None)  # Solicitações pendentes
    aceitas = FormServicos.objects.filter(aceita=True)    # Solicitações aceitas
    recusadas = FormServicos.objects.filter(aceita=False)
    return render(request, 'administrador.html', context={'pendentes': pendentes, 'aceitas': aceitas, 'recusadas': recusadas})

def inicio(request):
    return render(request, 'index.html')

def editar(request, id):
    formularios = FormServicos.objects.get(id=id)
    
    if request.method == "POST":
        form = formulario(request.POST, instance=formularios)
        if form.is_valid():
            form.save()
            return redirect('pedidos')
    else:
        form = formulario(instance=formularios)
    
    return render(request, 'contato.html', context={'form': form})

def deletar(request, id):
    form = FormServicos.objects.get(id=id)
    form.delete()
    return redirect('pedidos')

def aceitar_servico(request, id):
    servico = get_object_or_404(FormServicos, pk=id)
    servico.aceita = True  # Marca como aceita
    servico.save()
    return redirect('administrador')  # Redireciona para a página adequada

def recusar_servico(request, id):
    servico = get_object_or_404(FormServicos, pk=id)
    servico.aceita = False  # Marca como recusada
    servico.save()
    return redirect('administrador')