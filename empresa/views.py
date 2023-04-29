from . import serializers
from . import models 
from rest_framework import generics

class produtoView(generics.ListCreateAPIView):
    queryset= models.produto.objects.all()
    serializer_class= serializers.produtoSerializer
class produtosView(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.produto.objects.all()
    serializer_class= serializers.produtoSerializer
    
class variaView(generics.ListCreateAPIView):
    queryset= models.Variacao.objects.all()
    serializer_class= serializers.variaSerializer
class variasView(generics.ListCreateAPIView):
    queryset= models.Variacao.objects.all()
    serializer_class= serializers.variaSerializer