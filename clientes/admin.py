from django.contrib import admin
from . import models


class ItemPedidoInline(admin.TabularInline):
    model= models.ItemPedidos
    extra = 1

class pedidoAdmin(admin.ModelAdmin):
    inlines= [ItemPedidoInline]


admin.site.register(models.Pedido, pedidoAdmin)
admin.site.register(models.ItemPedidos)





#@admin.register(models.Pedido, pedidoAdmin)
#class pedidoAdmin(admin.ModelAdmin):
   # list_display=('usuario', 'total', 'status')



#@admin.register(models.ItemPedidos)
#class itemPedidosAdmin(admin.ModelAdmin):
 #   list_display=('pedido', 'nome_produto', 'produto_id','variacao', 'variacao_id', 'preco', 'imagem')