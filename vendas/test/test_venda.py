from django.test import TestCase

from produtos.models import Produto
from vendas.models import Venda, ItemDoPedido


class VendaTestCase(TestCase):
    def setUp(self):
        self.venda = Venda.objects.create(numero="1234", desconto=10, status=Venda.ABERTA)
        self.produto = Produto.objects.create(descricao="Produto 1", preco=10)
        self.item = ItemDoPedido.objects.create(venda=self.venda, produto=self.produto, quantidade=10, desconto=10)

    def test_verifica_num_vendas(self):
        assert Venda.objects.all().count() == 1

    def test_valor_venda(self):
        """Verifica valor total da venda"""

        assert self.venda.valor == 80

    def test_desconto(self):
        assert self.venda.desconto == 10

    def test_item_inlcuido_lista_itens(self):
        self.assertIn(self.item, self.venda.itemdopedido_set.all())

    def test_checa_nfe_nao_emitida(self):
        self.assertFalse(self.venda.nfe_emitida)

    def test_checa_status(self):
        self.venda.status = Venda.PROCESSANDO
        self.venda.save()
        self.assertEqual(self.venda.status, Venda.PROCESSANDO)
