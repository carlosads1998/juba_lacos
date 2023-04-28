from django.contrib import admin
from . import models

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1
    
class produtosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao','get_preco_pomocional', 'get_preco_formatado']
    
    inlines=[
        VariacaoInline
    ]



admin.site.register(models.produto, produtosAdmin)
admin.site.register(models.Variacao)