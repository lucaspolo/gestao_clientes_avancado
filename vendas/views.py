from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from vendas.models import Venda, ItemDoPedido
from .forms import ItemPedidoForm, ItemDoPedidoModelForm


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
        data['desconto'] = float(request.POST['desconto'].replace(',', '.'))
        data['venda_id'] = request.POST['venda_id']

        if data['venda_id']:
            venda = Venda.objects.get(id=data['venda_id'])
            venda.desconto = data['desconto']
            venda.numero = data['numero']
            venda.save()
        else:
            venda = Venda.objects.create(
                numero=data['numero'],
                desconto=data['desconto']
            )

        itens = venda.itemdopedido_set.all()
        data['venda'] = venda
        data['itens'] = itens

        return render(request, 'vendas/novo-pedido.html', data)


class NovoItemPedido(View):

    def get(self, request, pk):
        pass

    def post(self, request, venda):
        data = {}
        item = None

        if ItemDoPedido.objects.filter(produto_id=request.POST['produto_id']).exists():
            item = ItemDoPedido.objects.get(produto_id=request.POST['produto_id'])
            item.quantidade += float(request.POST['quantidade'])
            item.desconto = float(request.POST['desconto'])
            item.save()
        else:
            item = ItemDoPedido.objects.create(
                produto_id=request.POST['produto_id'], quantidade=request.POST['quantidade'],
                desconto=request.POST['desconto'], venda_id=venda
            )

        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itemdopedido_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data
        )


class ListaVendas(View):
    def get(self, request):
        vendas = Venda.objects.all()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas})


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        venda = Venda.objects.get(id=venda)
        data['form_item'] = ItemPedidoForm()
        data['numero'] = venda.numero
        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        data['itens'] = venda.itemdopedido_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data
        )


class DeletePedido(View):
    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        return render(request, 'vendas/delete-pedido-confirm.html', {'venda': venda})

    def post(self, request, venda):
        venda = Venda.objects.get(id=venda)
        venda.delete()
        return redirect('lista-vendas')


class DeleteItemPedido(View):
    def get(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        return render(request, 'vendas/delete-itempedido-confirm.html', {'item_pedido': item_pedido})

    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        venda_id = item_pedido.venda_id
        item_pedido.delete()
        return redirect('edit-pedido', venda=venda_id)


class EditItemPedido(View):
    def get(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        form = ItemDoPedidoModelForm(instance=item_pedido)
        return render(request, 'vendas/edit-itempedido.html', {'item_pedido': item_pedido, 'form': form})

    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        item_pedido.desconto = request.POST['desconto']
        item_pedido.quantidade = request.POST['quantidade']

        item_pedido.save()

        venda_id = item_pedido.venda_id
        return redirect('edit-pedido', venda=venda_id)
