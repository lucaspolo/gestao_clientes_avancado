from django.contrib import admin
from .models import Person, Documento, Venda, Produto


class PersonAdmin(admin.ModelAdmin):
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
    list_display = ['nome_completo', 'age', 'salary', 'bio', 'photo', 'doc']

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
