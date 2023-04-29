from . import models
from rest_framework import serializers


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.perfil
        fields= ('__all__')