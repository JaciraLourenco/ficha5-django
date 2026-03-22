from django.contrib import admin

from django.contrib import admin
from .models import Categoria, Produto, Morada, Pedido, ItemPedido

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Morada)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
