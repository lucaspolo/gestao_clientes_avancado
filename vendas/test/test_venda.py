from django.test import TestCase
from vendas.models import Venda


class VendaTestCase(TestCase):
    def setUp(self):
        Venda.objects.create(numero="1234")

    def test_verifica_num_vendas(self):
        assert Venda.objects.all().count() == 1
