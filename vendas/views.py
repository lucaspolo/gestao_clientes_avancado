from django.db.models import Avg
from django.shortcuts import render

from django.views import View

from vendas.models import Venda


class DashboardView(View):
    def get(self, request):
        media = Venda.objects.all().aggregate(Avg('valor'))['valor__avg']
        valores = {
            'media': media,
        }
        return render(request, 'vendas/dashboard.html', valores)
