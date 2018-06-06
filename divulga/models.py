from django.db import models
from django.apps import apps
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

# class Divulgacoes(models.Model):
#     nomeEvento = models.CharField(max_length=140, null=False)
#     telefone = models.CharField(max_length=140, null=False)
#     cidade = models.CharField(max_length=140, null=False)
#     #bairro = models.CharField(max_length=140, null=False)
#     endereco = models.CharField(max_length=140, null=False)
#     #cep = models.CharField(max_length=140, null=False)
#     horarioInicio = models.CharField(max_length=20, null=False)
#     horarioFim = models.CharField(max_length=20, null=False)
#     data = models.CharField(max_length=20, null=False)
#     categoria = models.CharField(max_length=50, null=False)
#     #data = models.DateTimeField(auto_now=False, auto_now_add=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

class Establishment(models.Model):
    name = models.CharField(max_length=50, null=False)
    openHour = models.TimeField()
    closeHour = models.TimeField()
    telefone = models.CharField(max_length=15, null=False)
    cidade = models.CharField(max_length=30, null=False)
    bairro = models.CharField(max_length=50, null=False)
    endereco = models.CharField(max_length=140, null=False)
    cep = models.CharField(max_length=10, null=False)
    categoria = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class CommunityAction(PolymorphicModel):
    name = models.CharField(max_length=50, null=False)
    start_date = models.DateField()
    close_date = models.DateField()
    description = models.CharField(max_length=500, null=False) 
    establishment = models.ManyToManyField(Establishment)

    def __str__(self):
        return self.name


class Donation(CommunityAction):
    item_name = models.CharField(max_length=50, null=False)
    amount = models.IntegerField()

class HealthService(CommunityAction):
    start_hour = models.TimeField()
    close_hour = models.TimeField()
 
