from django.db import models
from .Ativo import Ativo
# Create your models here.


class Cota(models.Model):
    ativo = models.ForeignKey(Ativo , on_delete=models.CASCADE)
    data = models.DateTimeField()
    valor = models.FloatField()
