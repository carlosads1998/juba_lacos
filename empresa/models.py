from django.contrib import admin
import os
from PIL import Image
from django.db import models
from .opcoes import Choices_tipo
from django.utils.text import slugify
from django.conf import settings


class produto(models.Model):
    nome= models.CharField(max_length=100)
    descricao= models.TextField(max_length=255)
    imagem= models.ImageField(upload_to='imagens_produtos/%Y/%m/', blank=True, null=True)
    slug= models.SlugField(unique=True, blank=True, null=True)
    preco= models.FloatField()
    preco_pomocional= models.FloatField(default=0)
    tipo= models.CharField(default='V', max_length=1,choices=Choices_tipo)
    
    def get_preco_formatado(self):
        return f'R$ {self.preco:.2f}'.replace('.', ',')
    get_preco_formatado.short_description = 'Preço'
    def get_preco_pomocional(self):
        return f'R$ {self.preco_pomocional:.2f}'.replace('.', ',')
    get_preco_pomocional.short_description = 'Preço Promocional'
    
    
    
    
    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil=Image.open(img_full_path)
        original_width, original_height = img_pil.size
        
        if original_width >= new_width:
            print('retornando, largura original menorque nova largura')
            img_pil.close()
            return
        
        new_height= round((new_width * original_height) / original_width)
        
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        max_image_size = 800
    
        if self.imagem:
            self.resize_image(self.imagem, max_image_size)
            
        def save (self, *args, **kwargs):
            if not self.slug:
                 slug= f'{slugify(self.nome)}'
                 self.slug= slug
    
    def __str__(self):
        return self.nome

class Variacao(models.Model):
    produto = models.ForeignKey(produto, on_delete=models.CASCADE)
    nome= models.CharField(max_length=50)
    preco= models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.nome or self.produto.nome
    
    class Meta:
        verbose_name= 'Variação'
        verbose_name_plural= 'Variações'