from . import models
from rest_framework import serializers

class pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Pedido
        fields = ('__all__')

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ItemPedidos
        fields = ('__all__') 