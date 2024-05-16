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
        return Articulo.objects.all()
    
class ArticuloViewsets(viewsets.ModelViewSet):
    serializer_class = ArticuloSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tipo = self.request.query_params.get('tipo', None)
        if tipo:
            return Articulo.objects.filter(tipo=tipo)
        else:
            return Articulo.objects.all()


