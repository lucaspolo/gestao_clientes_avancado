from django import forms

from vendas.models import ItemDoPedido


class ItemPedidoForm(forms.Form):
    produto_id = forms.CharField(label='ID do Produto', max_length=100)
    quantidade = forms.IntegerField(label="Quantidade")
    desconto = forms.DecimalField(label="Desconto", max_digits=7, decimal_places=2)


class ItemDoPedidoModelForm(forms.ModelForm):
    class Meta:
        model = ItemDoPedido
        fields = ['quantidade', 'desconto',]