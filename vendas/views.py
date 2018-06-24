from django.db.models import Avg, Min, Max, Count
from django.shortcuts import render

from django.views import View

from vendas.models import Venda


class DashboardView(View):
    def get(self, request):
        media = Venda.objects.all().aggregate(Avg('valor'))['valor__avg']
        media_desc = Venda.objects.all().aggregate(Avg('desconto'))['desconto__avg']
        min = Venda.objects.all().aggregate(Min('valor'))['valor__min']
        max = Venda.objects.all().aggregate(Max('valor'))['valor__max']
        numero_de_pedidos = Venda.objects.all().aggregate(Count('id'))['id__count']
        numero_de_pedidos_nfe_emitida = Venda.objects.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']

        data = {
            'media': media,
            'media_desc': media_desc,
            'min': min,
            'max': max,
            'numero_de_pedidos': numero_de_pedidos,
            'numero_de_pedidos_nfe_emitida': numero_de_pedidos_nfe_emitida,
        }
        return render(request, 'vendas/dashboard.html', data)
