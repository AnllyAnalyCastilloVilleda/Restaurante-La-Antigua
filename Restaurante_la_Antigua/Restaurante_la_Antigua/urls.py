from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from  Restaurante.views import *
from  Restaurante.viewsets import *

router = routers.DefaultRouter()
router.register(r"articulos", ArticuloViewsets, basename="articulo")
router.register(r"carritos", CarritoViewSets, basename="carritos")
router.register(r"carrito-cambiar-estado", CarritoCambiarEstadoViewSets, basename="carritos-cambiar-estado")
router.register(r"items_carrito", ItemCarritoViewSets, basename="items_carrito")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name ="inicio"),
    path('menu/', menu, name="menu"),
    path('pedidos/', pedidos, name="pedidos"),
    path('', home, name="home"),
    path('API/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls"))
]

