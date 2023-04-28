from django.urls import path
from . import views

app_name= 'pedido'

urlpatterns = [
    path('pagar/', views.Pagar.as_view(), name='Pagar'),
    path('fecharpedido/', views.FecharPedido.as_view(), name='Fechar_Pedido'),
    path('detalhe/', views.Detalhe.as_view(), name='Detalhe'),
]
