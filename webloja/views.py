from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden
from webloja.models import Produto 
from django import forms
from webloja.forms import ContatoForm, ProdutoForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'base.html')

@login_required
def produtos(request):
    lista_produtos = Produto.objects.all()
    return render(request, "produtos.html",{'produtos': lista_produtos})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form = ContatoForm()
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form':form})
    
@login_required
def cadastrar_produto(request):
    if request.user.tipo !='ADMIN':
        return HttpResponseForbidden('Apenas Administradores podem cadastrar produtos')
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.cadastrado_por = request.user
            produto.save()
            return redirect('produtos:listar')
    else:
        form = ProdutoForm()
    return render(request, 'produto_forms.html',
    {'form': form})