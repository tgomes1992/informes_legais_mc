from django.shortcuts import render
from cadastros.forms import *


# Create your views here.

def main_page(request):

    return render(request , "main.html")


def cadastro_ativos(request):
    context =  {
        "form": AtivosForm
    }
    return render(request , "cadastros/ativos.html" , context)


def cadastro_cotas(request):
    context =  {
        "form": CotasForm
    }
    return render(request , "cadastros/cotas.html" , context)

def cadastro_fundos(request):
    context =  {
        "form": FundosForm
    }
    return render(request , "cadastros/fundos.html", context )