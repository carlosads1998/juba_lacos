from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ListaProdutos(ListView):
    model=models.produto
    template_name= 'produto/lista.html'
    

class DetalheProduto(View):
    def get(sekf, *args, **kwargs):
        return HttpResponse('DetalheProduto')
    

class AdicionarAoCarrinho(View):
    def get(sekf, *args, **kwargs):
        return HttpResponse('AdicionarAoCarrinho')

class RemoverDoCarrinho(View):
    def get(sekf, *args, **kwargs):
        return HttpResponse('RemoverDoCarrinho')
    

class Carrinho(View):
    def get(sekf, *args, **kwargs):
        return HttpResponse('Carrinho')
    

class Finalizar(View):
    def get(sekf, *args, **kwargs):
        return HttpResponse('Finalizar')
    