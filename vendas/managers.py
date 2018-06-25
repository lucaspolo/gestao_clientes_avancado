from django.db import models
from django.db.models import Avg, Min, Max, Count


class VendaManager(models.Manager):

    def media(self):
        return self.all().aggregate(Avg('valor'))['valor__avg']

    def desconto_medio(self):
        return self.all().aggregate(Avg('desconto'))['desconto__avg']

    def venda_minima(self):
        return self.all().aggregate(Min('valor'))['valor__min']

    def venda_maxima(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def numero_de_pedidos(self):
        return self.all().aggregate(Count('id'))['id__count']

    def numero_de_pedidos_com_nfe_emitida(self):
        return self.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']
