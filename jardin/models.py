from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key = True)
    nombreProducto = models.CharField(max_length = 60)
    descripcion = models.CharField(max_length=255)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to = 'productos' ,null = True)

    def __str__(self) -> str:
        return self.nombreProducto

class Promocion(models.Model):
    idPromocion = models.IntegerField(primary_key = True)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    porc_descuento = models.IntegerField()
    fecha_caducidad = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.porc_descuento

# class Compra(models.Model):
#     idCompra = models.IntegerField(primary_key=True)
#     idCliente = models.CharField(max_length=200, null=True)
#     fechaCompra = models.DateTimeField(auto_now_add=True)
#     total = models.IntegerField()

#     def __str__(self) -> str:
#         return self.idCompra

# class DetalleCompra(models.Model):
#     idProducto = models.ForeignKey(Producto, on_delete= models.CASCADE)
#     cantidad = models.IntegerField(default = 1)
#     idCompra = models.ForeignKey(Compra, on_delete= models.CASCADE)

#     def __str__(self) -> str:
#         return self.idProducto.idProducto

# class Suscripcion(models.Model):
#     idUsuario = models.ForeignKey(User, on_delete= models.CASCADE)
#     email = models.CharField(max_length= 255)
#     fecha = models.DateTimeField(auto_now_add=True, null= True)

#     def __str__(self) -> str:
#         return self.email

class Suscripciones(models.Model):
    id_usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    email = models.CharField(max_length= 255)
    fecha = models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self) -> str:
        return self.email