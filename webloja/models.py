from django.db import models
from django.conf import settings

class Produto(models.Model):

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    cadastrado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
# Create your models here.
