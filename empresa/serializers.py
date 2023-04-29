from . import models
from rest_framework import serializers

class produtoSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.produto
        fields= ('__all__')
class variaSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Variacao
        fields= ('__all__')