from django.http import HttpResponseForbidden


def make_nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseForbidden('<h1>Ação não permitida</h1>')


make_nfe_emitida.short_description = "NF-e emitida"