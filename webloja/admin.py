from django.contrib import admin
from webloja.models import Produto
from clientes.models import Cliente


admin.site.register(Produto)
admin.site.register(Cliente)
# Register your models here.
