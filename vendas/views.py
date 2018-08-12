from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from vendas.models import Venda, ItemDoPedido
from .forms import ItemPedidoForm


class DashboardView(PermissionRequiredMixin, View):
    permission_required = ("vendas.ver_dashboard",)
    permission_denied_message = "Você não tem permissão de acesso para ver o Dashboard."

    # Não é mais necessário pois importa tem o PermissionRequiredMixin
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.has_perm('vendas.ver_dashboard'):
    #         return HttpResponse('<h1>Você não tem permissão para acessar este local.</h1>')
    #
    #     return super().dispatch(request, *args, **kwargs)

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

class NovoPedido(View):

    def get(self, request):
        return render(request, 'vendas/novo-pedido.html')

    def post(self, request):
        data = {}

        data['form_item'] = ItemPedidoForm()
        data['numero'] = request.POST['numero']
        data['desconto'] = float(request.POST['desconto'])
        data['venda'] = request.POST['venda_id']

        if data['venda']:
            venda = Venda.objects.get(id=data['venda'])
            venda.desconto = data['desconto']
            venda.numero = data['numero']
            venda.save()
        else:
            venda = Venda.objects.create(
                numero=data['numero'],
                desconto=data['desconto']
            )

        itens = venda.itemdopedido_set.all()
        data['venda_obj'] = venda
        data['itens'] = itens

        return render(request, 'vendas/novo-pedido.html', data)


class NovoItemPedido(View):

    def get(self, request, pk):
        pass

    def post(self, request, venda):
        data = {}

        item = ItemDoPedido.objects.create(
            produto_id=request.POST['produto_id'], quantidade=request.POST['quantidade'],
            desconto=request.POST['desconto'], venda_id=venda
        )

        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda.id
        data['venda_obj'] = item.venda
        data['itens'] = item.venda.itemdopedido_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data
        )

class ListaVendas(View):
    def get(self, request):
        vendas = Venda.objects.all()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas})
