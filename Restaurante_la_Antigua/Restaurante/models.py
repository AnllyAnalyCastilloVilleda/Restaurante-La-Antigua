from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    """ Modelo para el registro de Articulo """

    TIPO_CHOICES = [
        ('1', 'Comida'),
        ('2', 'Bebida'),
        ('3', 'Postre'),
    ]

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_inventario = models.IntegerField(default=0)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['tipo']

class Carrito(models.Model):
    """ Modelo para el registro de Carrito """
    ESTADO_CHOICES = [
        ('SinAceptar','SinAceptar'),
        ('En espera', 'En Espera'),
        ('Aceptado',  'Aceptado'),
        ('Terminado', 'Terminado'),
        ('Entregado', 'Entregado'),
    ]

    id = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(User, default=1, on_delete= models.CASCADE)
    mesa = models.IntegerField()
    pagado = models.BooleanField(default=False)
    estadopedido = models.CharField(default='sinAceptar', max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"Carrito {self.id} - Mesa {self.mesa}"

class ItemCarrito(models.Model):
    """ Modelo para los artículos en el carrito """

    id = models.AutoField(primary_key=True, unique=True)
    cantidad = models.PositiveIntegerField()
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cantidad}x {self.articulo.nombre} en Carrito {self.carrito.id}"
    

class Cliente(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
