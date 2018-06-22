from django.contrib import admin

# Register your models here.
from vendas.actions import make_nfe_emitida
from vendas.models import Venda, ItensDoPedido


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    list_filter = ('pessoa__doc', 'desconto',)
    list_display = ('id', 'pessoa', 'valor', 'nfe_emitida')
    autocomplete_fields = ('pessoa',)

    def get_total(self, obj: Venda):
        return obj.get_total()

    get_total.short_description = 'Valor total'

    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')

    actions = [make_nfe_emitida]

    # filter_horizontal = ['produtos',]


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)
