from django.contrib import admin
from .models import *

# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion", "precio", "cantidad_inventario", "tipo")

admin.site.register(Articulo, ArticuloAdmin)

class CarritoAdmin(admin.ModelAdmin):
    list_display = ("id",  "mesa", "pagado", "estadopedido")

admin.site.register(Carrito, CarritoAdmin)

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ("id", "cantidad", "carrito", "articulo")

admin.site.register(ItemCarrito, ItemCarritoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "direccion", "telefono")

admin.site.register(Cliente, ClienteAdmin)
