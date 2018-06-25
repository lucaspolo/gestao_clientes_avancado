from django.db import models

# Create your models here.
from django.db.models import Sum, F, FloatField
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from clientes.models import Person
from produtos.models import Produto
from vendas.managers import VendaManager


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    objects = VendaManager()

    def calcular_total(self):
        total = self.itemdopedido_set.all().aggregate(
            tot_pedido=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_pedido'] or 0

        total = total - float(self.impostos) - float(self.desconto)

        self.valor = total
        Venda.objects.filter(id=self.id).update(valor=total)

    def __str__(self):
        return self.numero


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.venda.numero} - {self.produto.descricao} ({self.quantidade})"


@receiver(post_save, sender=ItemDoPedido)
def update_item_do_pedido_total(sender, instance: ItemDoPedido, **kwargs):
    """
    Funcao que sera executada quando houver mudanca m2m
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.venda.calcular_total()


@receiver(post_save, sender=Venda)
def update_vendas_total(sender, instance: Venda, **kwargs):
    instance.calcular_total()
