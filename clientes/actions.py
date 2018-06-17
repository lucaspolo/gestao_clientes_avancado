def make_nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)

make_nfe_emitida.short_description = "NF-e emitida"