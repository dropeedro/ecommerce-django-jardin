from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *
from jardin.carrito import Carrito
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    contexto = {'productos': Producto.objects.all()[:4]}
    return render(request, 'index.html', contexto)

@login_required(login_url='login')
def mostrarProductos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'crud_productos.html', contexto)


def catalogo_productos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'catalogo_productos.html', contexto)

@login_required(login_url='login')
def misCompras(request):
    return render(request, 'misCompras.html')


def login(request):
    return render(request, 'login.html')

#crea productos (crud) 

@login_required(login_url='login')
def crearProducto(request):
    datos = {
        "form": ProductoForm()
        }
    if request.method == "POST":
        form = ProductoForm(data = request.POST, files = request.FILES)
        if form.is_valid:
            form.save()
            return redirect(to = "listar_productos")
        else:
            datos["form"] = form
    return render(request, 'crud_productos.html', datos)

#crea promociones (crud) 
@login_required(login_url='login')
def crearPromociones(request):
    datos = {
        "form": PromocionesForm()
        }
    if request.method == 'POST':
        form = PromocionesForm(data = request.POST)
        if form.is_valid:
            form.save()
            return redirect(to = "listar_promociones")
        else:
            datos["form"] = form
    return render(request, 'crud_promociones.html', datos)

#registra usuario
def registro(request):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        messages.success(request, f'Usuario {username} ha sido creado')
        return redirect('/jardin/')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'registro.html', context)


## CRUD PRODUCTOS
@login_required(login_url='login')
def listarProductos(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request, 'listar_productos.html', datos)

@login_required(login_url='login')
def modificarProducto(request, id):
    producto = get_object_or_404(Producto, idProducto = id)
    datos = {
        'form': ProductoForm(instance = producto)
    }

    if request.method == "POST":
        formulario = ProductoForm(data = request.POST, instance = producto, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to = "listar_productos")
        datos["form"] = formulario


    return render(request, 'modificar_producto.html', datos)

@login_required(login_url='login')
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, idProducto = id)
    producto.delete()
    return redirect(to = "listar_productos")


## CRUD PROMOCIONES 
@login_required(login_url='login')
def listarPromociones(request):
    promociones = Promocion.objects.all()
    datos = {
        'promociones' : promociones
    }
    return render(request, 'listar_promociones.html', datos)

@login_required(login_url='login')
def modificarPromocion(request, id):
    promociones = get_object_or_404(Promocion, idpromociones = id)
    datos = {
        'form': PromocionesForm(instance = promociones)
    }

    if request.method == "POST":
        formulario = PromocionesForm(data = request.POST, instance = promociones, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to = "listar_promocioness")
        datos["form"] = formulario


    return render(request, 'modificar_promociones.html', datos)

@login_required(login_url='login')
def eliminarPromocion(request, id):
    promociones = get_object_or_404(Promocion, idPromocion = id)
    promociones.delete()
    return redirect(to = "listar_promociones")

#CARRITO DE COMPRAS
def carrito(request):
    productos = Producto.objects.all()
    return render(request, "plantilla_menu.html", {'productos' : productos})

@login_required(login_url='login')
def agregarProducto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = producto_id)
    carrito.agregar(producto)
    if request.user.is_authenticated:
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('index')

@login_required(login_url='login')
def eliminarProducto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = producto_id)
    carrito.eliminar(producto)
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def restarProducto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = producto_id)
    carrito.restar(producto)
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(request.META['HTTP_REFERER'])

## crea suscripcion
def creaSuscripcion(request):
    user = request.user
    datos = {
        "form":  SuscripcionForm()
       }
    if request.method == "POST":
        form = SuscripcionForm(request.POST)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.id_usuario = user
            obj.save()
            return redirect(to = "index")
        else:
            datos["form"] = form
    return render(request, 'suscripciones.html', datos)