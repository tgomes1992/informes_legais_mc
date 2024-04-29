from django.db import models

# Create your models here.


class Fundo(models.Model):
    TIPO_CHOICES = (
        ('A', 'Aberto'),
        ('F', 'Fechado'),
    )
    cnpj = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=1,choices=TIPO_CHOICES)