from dataclasses import fields
from tkinter import Widget
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
                'idProducto',
                'nombreProducto',
                'descripcion',
                'precio',
                'stock',
                'imagen'
                ]

class PromocionesForm(ModelForm):
    class Meta:
        model = Promocion
        fields = [
            'idPromocion',
            'id_producto',
            'porc_descuento',
            'fecha_caducidad',
        ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña: ', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña: ', widget = forms.PasswordInput)
    nombre = forms.CharField(label='Nombre Completo: ')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k:"" for k in fields}

class SuscripcionForm(ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Suscripciones
        fields = ['email']