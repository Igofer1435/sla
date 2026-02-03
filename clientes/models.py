from django.db import models
from django.conf import settings


# Create your models here.
class Cliente(models.Model):
    Cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cadastrado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    
    def __str__(self):
        return self.Cpf