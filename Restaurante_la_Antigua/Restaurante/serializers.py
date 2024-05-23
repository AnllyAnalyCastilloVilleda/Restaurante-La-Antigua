from rest_framework import serializers
from .models import *

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Articulo
        fields = "__all__"

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = "__all__"
        read_only_fields = ("id", "usuario")

    def create(self, validated_data):
        objeto = Carrito.objects.create(
            usuario = self.context["request"].user,
            mesa = validated_data["mesa"]
        )
        return objeto
    
class ItemCarritoSerializer(serializers.ModelSerializer):

    articulo = ArticuloSerializer(read_only=True)
    idArticulo = serializers.PrimaryKeyRelatedField(queryset=Articulo.objects.all(), source="articulo", write_only=True)

    class Meta:
        model = ItemCarrito
        fields = "__all__"
        