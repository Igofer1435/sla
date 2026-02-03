from django.shortcuts import render, redirect
from django.http import HttpResponse
from clientes.models import Cliente
from clientes.forms import ClienteForm
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from clientes.models import Cliente
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#FBV
def home(request):
    return render(request, "base.html")

@login_required
def clientes(request):
    lista_clientes = Cliente.objects.all()
    contexto = {'clientes': lista_clientes}
    return render(request, "clientes.html",contexto)

@login_required
def cadastrar_cliente(request):
    if request.user.tipo !='ADMIN':
        return HttpResponseForbidden('Apenas Administradores podem cadastrar clientes')
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.cadastrado_por = request.user
            cliente.save()
            return redirect('clientes:listar')
    else:
        form = ClienteForm()
    return render(request, 'cliente_forms.html',
    {'form': form})

#CBV
class ClientesListView(LoginRequiredMixin, ListView):
    template_name = "clientes.html"
    model = Cliente
    context_object_name = "clientes"

class ClientesCreateView(LoginRequiredMixin, CreateView):
    template_name = "cliente_forms.html"
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("clientes:listar")
    
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.tipo != 'ADMIN':
            return HttpResponseForbidden("Você não tem permissão para cadastrar clientes.")
        return super().dispatch(request, *args, **kwargs)
