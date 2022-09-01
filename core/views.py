from django.shortcuts import render, redirect
from .models import Acessorios, Camisas, Calcados, Short
from .forms import CamisasForm, CalcadosForm, ShortForm, AcessoriosForm

# Create your views here.

#Crud de Camisas
def camisas_listar(request):
    camisa = Camisas.objects.all()
    contexto = {
        'listar_camisas' : camisa
    }
    return render(request,'' , contexto)

def camisas_cadastrar(request):
    form = CamisasForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('')
    contexto = {
        'form': form
    }
    return render(request, '', contexto)

def camisas_editar(request,id):


def camisas_remover(request,id):
    

#Crud de Short
def short_listar(request):
    short = Short.objects.all()
    contexto = {
        'listar_shorts' : short
    }
    return render(request,'' , contexto)

def short_cadastrar(request):
    form = ShortForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('')
    contexto = {
        'form': form
    }
    return render(request, '', contexto)

def short_editar(request,id):


def short_remover(request,id):


#Crud de Calçados
def calcados_listar(request):
    calcado = Calcados.objects.all()
    contexto = {
        'listar_calcados' : calcado
    }
    return render(request,'' , contexto)

def calcados_cadastrar(request):
    form = CalcadosForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('')
    contexto = {
        'form': form
    }
    return render(request, '', contexto)

def calcados_editar(request,id):


def calcados_remover(request,id):


#Crud de Acessorios
def acessorios_listar(request):
    acessorio = Acessorios.objects.all()
    contexto = {
        'listar_acessorios' : acessorio
    }
    return render(request,'' , contexto)

def acessorios_cadastrar(request):
    form = AcessoriosForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('')
    contexto = {
        'form': form
    }
    return render(request, '', contexto)

def acessorios_editar(request,id):


def acessorios_remover(request,id):
