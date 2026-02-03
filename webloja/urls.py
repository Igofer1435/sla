from django.urls import path, include
from .views import home,produtos,contato,cadastrar_produto

app_name= 'produtos'

urlpatterns = [
    path('', home, name='home'),
    path('faleconosco/',contato, name= 'contato'),
    path('listar/',produtos, name='listar'),
    path('cadastrar/',cadastrar_produto, name= 'cadastrar'),

]