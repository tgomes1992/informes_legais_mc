from django.forms import ModelForm
from cadastros.models import *


class AtivosForm(ModelForm):
    class Meta:
        model = Ativo
        fields = ['fundo' , "cd_jcot" , "cd_o2" , "cd_amplis"]


class CotasForm(ModelForm):
    class Meta:
        model = Cota
        fields = ['ativo' , "data" , "valor"]



class FundosForm(ModelForm):
    class Meta:
        model = Fundo
        fields = ['cnpj' , "nome" , "tipo"]


