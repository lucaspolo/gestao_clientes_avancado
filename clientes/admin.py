from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Person, Documento, Venda, Produto


class PersonAdmin(admin.ModelAdmin):
    """
    Classe sobrescreve o padrão do Admin para Person
    """

    # Irá descrever como os dados são apresentados em telas de cadastro
    fieldsets = (
        (
            'Dados pessoais',
            {
                'fields': ('doc', 'first_name', 'last_name',)
            }
        ),
        (
            'Dados complementares',
            {
                'fields': ('age', 'salary', 'bio', 'photo',)
            }
        )
    )
    # fields = ['doc', ('first_name', 'last_name'), ('age', 'salary'), 'bio', 'photo']
    list_display = ['nome_completo', 'age', 'salary', 'bio', 'photo', 'doc'] #Descreve quais dados são exibidos

    class SalaryListFilter(admin.SimpleListFilter):
        """
        Esta classe permite que seja criado filtros para o Django Admin
        """
        title = _('Faixa salarial') # Titulo exibido
        parameter_name =  'salary' # Parametro que se baseia o filtro

        def lookups(self, request, model_admin):
            """
            Define quais os nomes das faixas e suas descrições (estas exibidas em tela)
            :param request:
            :param model_admin:
            :return:
            """
            return (
                ('<10000', _('Menor que 10 mil')),
                ('>=10000', _('Maior ou igual a 10 mil')),
            )

        def queryset(self, request, queryset):
            """
            Método que efetivamente filtra, chamado uma vez para cada faixa
            :param request:
            :param queryset:
            :return:
            """
            if self.value() == '<10000':
                return queryset.filter(salary__lt = 10000)

            if self.value() == '>=10000':
                return queryset.filter(salary__gte=10000)

    list_filter = (SalaryListFilter, )


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
