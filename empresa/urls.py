from django.urls import path
from . import views

app_name= 'empresa'

urlpatterns = [
    path('produto', views.produtoView.as_view(), name='Produto'),
    path('produtos/', views.produtosView.as_view(), name= 'Produtos'),
    path('variacao/', views.variaView.as_view(), name= 'variação'),
    path('variacoes/', views.variasView.as_view(), name='variações'),
]
