from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from  django.db.models.query import QuerySet
from django.db.models import Case, When, Value, IntegerField


from .models import * 
from .serializers import *

#Los Viwsets son los objetos de un modelo que quiero mostrar en la API 

class ArticuloViewsets(viewsets.ModelViewSet):
    serializer_class = ArticuloSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tipo = self.request.query_params.get('tipo', None)
        if tipo:
            return Articulo.objects.filter(tipo=tipo)
        else:
            return Articulo.objects.all()

class CarritoViewSets(viewsets.ModelViewSet):
    serializer_class = CarritoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        estado = self.request.query_params.get('estado', None)

        if estado:
            return Carrito.objects.filter(estadopedido=estado)
        else:
            return Carrito.objects.all()
        
class CarritoCambiarEstadoViewSets(viewsets.ModelViewSet):
    serializer_class = CarritoCambiarEstadoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Carrito.objects.all()

class ItemCarritoViewSets(viewsets.ModelViewSet):
    serializer_class = ItemCarritoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idCarrito = self.request.query_params.get('carrito')
        return ItemCarrito.objects.filter(carrito=idCarrito)
