from django.urls import path
from . import views

app_name= 'empresa'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='Lista'),
    path('<slug>', views.DetalheProduto.as_view(), name= 'detalhe'),
    path('adicionarcarrinho/', views.AdicionarAoCarrinho.as_view(), name= 'Adicionar_ao_Carrinho'),
    path('removerdocarrinho/', views.RemoverDoCarrinho.as_view(), name='removerdocarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='Carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='Finalizar'),
]
