from django.db import models
from django.contrib.auth.models import User
from .opcoes import CHOICES_STATUS

class Pedido(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    total= models.FloatField()
    status= models.CharField(default='C', max_length=1,choices=CHOICES_STATUS)
    
    def __str__(self):
        return f'Pedido N. {self.pk}'
    
class ItemPedidos(models.Model):
    pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nome_produto=models.CharField(max_length=255)   
    produto_id=models.IntegerField()
    variacao=models.CharField(max_length=255)
    variacao_id=models.PositiveIntegerField()
    preco=models.FloatField()
    imagem= models.CharField(max_length=2000) 
    
    def __str__(self):
        return f'Item do {self.pedido}'
    
    class Meta:
        verbose_name= 'Item Pedido'
        verbose_name_plural= 'Itens Pedidos'