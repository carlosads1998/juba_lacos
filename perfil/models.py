from django.db import models
from django.contrib.auth.models import User
from .opcoes import choices_estado
from django.forms import ValidationError
import re
from utils.validador import valida_cpf


class perfil(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    idade=models.PositiveIntegerField(null=True)
    data_nascimento = models.DateField()
    cpf= models.CharField(max_length=11)
    endereco= models.CharField(max_length=50)
    numero= models.CharField(max_length=5)
    complemento=models.CharField(max_length=35)
    bairro=models.CharField(max_length=35)
    cep= models.CharField(max_length=8)
    cidade=models.CharField(max_length=30)
    estado= models.CharField(max_length=2, choices=choices_estado)
    
    def __str__(self):
        return f'{self.usuario}'
    
    def clean(self):
        error_messages= {}
        
        if not valida_cpf(self.cpf):
            error_messages['cpf']= 'Digite um CPF Válido'
        
        if re.search(r'[^0-9]', self.cep) or len(self.cep) <8:
            error_messages['cep']='CEP Inválido, digite os 8 dígitos do CEP'
            
        if error_messages:
            raise ValidationError(error_messages)
                
            
            
    class Meta:
        verbose_name= 'perfil'
        verbose_name_plural='perfis'