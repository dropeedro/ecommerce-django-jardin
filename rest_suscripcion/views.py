from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from jardin.models import Suscripciones
from .serializers import SuscripcionSerializer

@csrf_exempt
@api_view(['GET','POST', 'PUT', 'DELETE'])
def lista_suscripciones(request):
    """
    Lista todas las suscripciones 
    """
    # try:
    #     suscripcion = Suscripciones.objects.get(id = id)
    # except Suscripciones.DoesNotExist:
    #     return Response( status = status.HTTP_404_NOT_FOUND)
    suscripcion = Suscripciones.objects.all()
    if request.method == 'GET':
        serializer = SuscripcionSerializer(suscripcion, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuscripcionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SuscripcionSerializer(suscripcion, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        suscripcion.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)