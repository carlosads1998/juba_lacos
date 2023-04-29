from . import serializers
from . import models
from rest_framework import generics

class pedidoView(generics.ListCreateAPIView):
    queryset=models.Pedido.objects.all()
    serializer_class= serializers.pedidoSerializer
class pedidosView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Pedido.objects.all()
    serializer_class= serializers.pedidoSerializer

class itemView(generics.ListCreateAPIView):
    queryset=models.ItemPedidos.objects.all()
    serializer_class= serializers.itemSerializer
class itensView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.ItemPedidos.objects.all()
    serializer_class= serializers.itemSerializer
    