from rest_framework.serializers import ModelSerializer
from jardin.models import *
class SuscripcionSerializer(ModelSerializer):
    class Meta:
            model = Suscripciones
            fields = '__all__'