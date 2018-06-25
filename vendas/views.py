from django.db.models import Avg, Min, Max, Count
from django.shortcuts import render

from django.views import View

from vendas.models import Venda


class DashboardView(View):
    def get(self, request):
        media = Venda.objects.media()
        media_desc = Venda.objects.desconto_medio()
        min = Venda.objects.venda_minima()
        max = Venda.objects.venda_maxima()
        numero_de_pedidos = Venda.objects.numero_de_pedidos()
        numero_de_pedidos_nfe_emitida = Venda.objects.numero_de_pedidos_com_nfe_emitida()

        data = {
            'media': media,
            'media_desc': media_desc,
            'min': min,
            'max': max,
            'numero_de_pedidos': numero_de_pedidos,
            'numero_de_pedidos_nfe_emitida': numero_de_pedidos_nfe_emitida,
        }
        return render(request, 'vendas/dashboard.html', data)
