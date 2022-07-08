from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Promocion)
admin.site.register(Suscripciones)
# admin.site.register(Compra)
# admin.site.register(DetalleCompra)