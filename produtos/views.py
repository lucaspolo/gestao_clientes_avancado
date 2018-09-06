from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from produtos.models import Produto


def api(request):

    produtos = Produto.objects.all()

    lista_produtos = []
    for produto in produtos:
        lista_produtos.append(model_to_dict(produto))

    return JsonResponse({'produtos': lista_produtos})
