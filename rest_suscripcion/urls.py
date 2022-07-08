from django.urls import path
from rest_suscripcion.views import lista_suscripciones

urlpatterns = [
    path('lista_suscripciones', lista_suscripciones, name="lista_suscripciones")
]