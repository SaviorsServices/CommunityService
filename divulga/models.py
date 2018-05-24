from django.db import models
from django.apps import apps
from django.contrib.auth.models import User

class Divulgacoes(models.Model):
    nomeEvento = models.CharField(max_length=140, null=False)
    telefone = models.CharField(max_length=140, null=False)
    cidade = models.CharField(max_length=140, null=False)
    bairro = models.CharField(max_length=140, null=False)
    endereco = models.CharField(max_length=140, null=False)
    cep = models.CharField(max_length=140, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
