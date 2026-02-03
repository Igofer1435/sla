from django.urls import path, include
from clientes.views import home,clientes,cadastrar_cliente

app_name = 'clientes'

urlpatterns = [
    #Funcionais
    #path('', home, name='home'),
    #path('clientes/',clientes, name='listar'),
    #modificado
    path('',clientes, name='listar'),
    path('cadastrar/',cadastrar_cliente, name= 'cadastrar'),

]