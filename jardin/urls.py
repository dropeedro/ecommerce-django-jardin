from re import template
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

##URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo_productos/', views.catalogo_productos, name='catalogo_productos'),
    path('listar_productos/', views.listarProductos, name='listar_productos'),
    path('listar_promociones/', views.listarPromociones, name='listar_promociones'),
    path('crud_productos/', views.crearProducto, name='crud_productos'),
    path('crud_promociones/', views.crearPromociones, name='crud_promociones'),
    path('modificar_producto/<id>/', views.modificarProducto, name='modificar_producto'),
    path('modificar_promocion/<id>/', views.modificarPromocion, name='modificar_promocion'),
    path('eliminar_producto/<id>/', views.eliminarProducto, name='eliminar_producto'),
    path('eliminar_promocion/<id>/', views.eliminarPromocion, name='eliminar_promocion'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('misCompras/', views.misCompras, name='misCompras'),
    path('registro/', views.registro, name='registro'),
    path('agregar/<int:producto_id>/', views.agregarProducto_carrito, name="sumar"),
    path('eliminar/<int:producto_id>/', views.eliminarProducto_carrito, name="Eliminar"),
    path('restar/<int:producto_id>/', views.restarProducto_carrito, name="restar"),
    path('limpiar/', views.limpiarCarrito, name="Limpiar"),
    path('suscripciones/', views.creaSuscripcion, name='creaSuscripcion'),
]