from django.contrib import admin
from .models import Person, Documento, Venda, Produto


class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    list_display = fields

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
