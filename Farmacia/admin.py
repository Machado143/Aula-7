from django.contrib import admin
from . import models




class MedicamentoInline(admin.TabularInline):
    model = models.ClienteMedicamento
    extra = 0
    fields = ('medicamento', 'get_fornecedora')
    readonly_fields = ('get_fornecedora',)


    def get_fornecedora(self, obj):
        return obj.medicamento.fornecedora.nome if obj.medicamento.fornecedora else "-"
    get_fornecedora.short_description = 'Fornecedora'




@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [MedicamentoInline]
    list_display = ('nome', 'email', 'telefone')




@admin.register(models.Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'fornecedora')
    list_filter = ('fornecedora',)




@admin.register(models.Fornecedora)  
class FornecedoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'email')




admin.site.register(models.ClienteMedicamento)

admin.register(models.Post)



