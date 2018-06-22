from django.db import models

# Create your models here.
from clientes.models import Person
from produtos.models import Produto


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)


    # def get_total(self):
    #     total = 0
    #     for produto in self.produtos.all():
    #         total += produto.preco
    #
    #     return (total - self.desconto) - self.impostos

    def __str__(self):
        return self.numero


class ItensDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.venda.numero} - {self.produto.descricao} ({self.quantidade})"


# @receiver(m2m_changed, sender=Venda.produtos.through)
def update_vendas_total(sender, instance: Venda, **kwargs):
    """
    Funcao que sera executada quando houver mudanca m2m
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.valor = instance.get_total()
    instance.save()
    # total = instance.get_total()
    # venda.objects.filter(id=instance.id).update(total=total)