from django.shortcuts import render, redirect
from .models import Acessorios, Camisas, Calcados, Short
from .forms import CamisasForm, CalcadosForm, ShortForm, AcessoriosForm

# Create your views here.
def home(request):
    return render(request, 'index.html')



#Crud de Camisas
def camisas_listar(request):
    camisa = Camisas.objects.all()
    contexto = {
        'listar_camisas' : camisa
    }
    return render(request,'camisas.html' , contexto)

def camisas_cadastrar(request):
    form = CamisasForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('listar_camisas')
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_camisas.html', contexto)

def camisas_editar(request,id):
    camisa = Camisas.objects.get(pk=id)
    
    form = CamisasForm(request.POST or None, request.FILES or None, instance=camisa)
    if form.is_valid():
        form.save()
        return redirect('listar_camisas')
    
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_camisas.html', contexto)

def camisas_remover(request,id):
    camisas = Camisas.objects.get(pk=id)
    camisas.delete()
    return redirect('listar_camisas')

#Crud de Short
def short_listar(request):
    short = Short.objects.all()
    contexto = {
        'listar_shorts' : short
    }
    return render(request,'short.html' , contexto)

def short_cadastrar(request):
    form = ShortForm(request.POST or None,request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('listar_shorts')
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_short.html', contexto)

def short_editar(request,id):
    short = Short.objects.get(pk=id)
    
    form = ShortForm(request.POST or None,request.FILES or None,  instance=short)
    if form.is_valid():
        form.save()
        return redirect('listar_shorts')
    
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_short.html', contexto)

def short_remover(request,id):
    short = Short.objects.get(pk=id)
    short.delete()
    return redirect('listar_shorts')

#Crud de Calçados
def calcados_listar(request):
    calcado = Calcados.objects.all()
    contexto = {
        'listar_calcados' : calcado
    }
    return render(request,'calcados.html' , contexto)

def calcados_cadastrar(request):
    form = CalcadosForm(request.POST or None,request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('listar_calcados')
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_calcados.html', contexto)

def calcados_editar(request,id):
    calcados = Calcados.objects.get(pk=id)
    
    form = CalcadosForm(request.POST or None,request.FILES or None, instance=calcados)
    if form.is_valid():
        form.save()
        return redirect('listar_calcados')
    
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_calcados.html', contexto)

def calcados_remover(request,id):
    calcados = Calcados.objects.get(pk=id)
    calcados.delete()
    return redirect('listar_calcados')

#Crud de Acessorios
def acessorios_listar(request):
    acessorio = Acessorios.objects.all()
    contexto = {
        'listar_acessorios' : acessorio
    }
    return render(request,'acessorios.html' , contexto)

def acessorios_cadastrar(request):
    form = AcessoriosForm(request.POST or None,request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('listar_acessorios')
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_acessorios.html', contexto)

def acessorios_editar(request,id):
    acessorio = Acessorios.objects.get(pk=id)
    
    form = AcessoriosForm(request.POST or None,request.FILES or None, instance=acessorio)
    if form.is_valid():
        form.save()
        return redirect('listar_acessorios')
    
    contexto = {
        'form': form
    }
    return render(request, 'cadastrar_acessorios.html', contexto)

def acessorios_remover(request,id):
    acessorio = Acessorios.objects.get(pk=id)
    acessorio.delete()
    return redirect('listar_acessorios')