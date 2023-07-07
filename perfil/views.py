from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from .utils import calcula_total

def home(request):
    contas = Conta.objects.all()
    saldo_total = calcula_total(contas, 'valor')
    return render(request, 'home.html', {'contas': contas, 'saldo_total':saldo_total})
    

def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    total_conta = calcula_total(contas, 'valor')
    return render(request, 'gerenciar.html', {'contas': contas,'total_conta':total_conta,'categorias':categorias})


def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('gerenciar')
    # FAZER MAIS VALIDAÇÕES
    
    conta = Conta(
        apelido= apelido,
        banco= banco,
        tipo = tipo,
        valor= valor,
        icone= icone
    )
    conta.save()
    messages.add_message(request, constants.SUCCESS, 'Conta Cadastrada com sucesso!')
    return redirect('gerenciar')

def deletar_banco(request, id):
    conta = get_object_or_404(Conta, pk=id)
    conta.delete()
    messages.add_message(request, constants.SUCCESS, 'Conta removida com sucesso!') 
    return redirect('gerenciar')

def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))
    
    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )
    categoria.save()
    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso!')
    return redirect('gerenciar')


def update_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    categoria.essencial = not categoria.essencial
    categoria.save()
    return redirect('gerenciar')