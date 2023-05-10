from django.contrib import admin
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    search_fields = ('id', 'tipo_pedido', 'direccion', 'conductor_id', 'fecha', 'hora')
    list_display = ('id', 'tipo_pedido', 'direccion', 'conductor', 'fecha', 'hora')
    raw_id_fields = ('conductor_id',)
    ordering = ('fecha',)
    list_filter = ('tipo_pedido', 'fecha', 'estado')

admin.site.register(Pedido, PedidoAdmin)

