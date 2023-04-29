from . import serializers
from . import models
from rest_framework import generics


class perfilView(generics.ListCreateAPIView):
    queryset= models.perfil.objects.all()
    serializer_class=serializers.PerfilSerializer
class perfisView(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.perfil.objects.all()
    serializer_class=serializers.PerfilSerializer