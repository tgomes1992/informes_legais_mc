from django.db import models
from .Fundo import Fundo
# Create your models here.


class Ativo(models.Model):
    fundo = models.ForeignKey(Fundo, on_delete=models.CASCADE)
    cd_jcot = models.CharField(max_length=25 , default="")
    cd_o2 = models.CharField(max_length=200 , default="")
    cd_amplis = models.CharField(max_length=250 , default="", null=True)
