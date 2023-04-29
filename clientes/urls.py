from django.urls import path
from . import views


urlpatterns = [
    path('pedido/', views.pedidoView.as_view(), name= 'Pedido'),
    path('pedidos/', views.pedidosView.as_view(), name= 'Pedidos'),
    path('item/', views.itemView.as_view(), name= 'Pedido'),
    path('itens/', views.itensView.as_view(), name= 'Pedido'),
]
