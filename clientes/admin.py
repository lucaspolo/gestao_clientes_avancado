from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Person, Documento


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

    search_fields = ('id', 'first_name', 'last_name',)

    list_display = ['nome_completo', 'age', 'salary', 'bio', 'tem_foto', 'doc']  # Descreve quais dados são exibidos

    def tem_foto(self, obj: Person):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_foto.short_description = "Possui foto?"

    class SalaryListFilter(admin.SimpleListFilter):
        """
        Esta classe permite que seja criado filtros para o Django Admin
        """
        title = _('Faixa salarial')  # Titulo exibido
        parameter_name = 'salary'  # Parametro que se baseia o filtro

        def lookups(self, request, model_admin):
            """
            Define quais os nomes das faixas e suas descrições (estas exibidas em tela)
            """
            return (
                ('<10000', _('Menor que 10 mil')),
                ('>=10000', _('Maior ou igual a 10 mil')),
            )

        def queryset(self, request, queryset):
            """
            Método que efetivamente filtra, chamado uma vez para cada faixa
            """
            if self.value() == '<10000':
                return queryset.filter(salary__lt=10000)

            if self.value() == '>=10000':
                return queryset.filter(salary__gte=10000)

    list_filter = (SalaryListFilter,)


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
