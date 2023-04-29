from django.urls import path
from . import views


urlpatterns = [
    path('perfil/', views.perfilView.as_view(), name='Criar'),
    path('atualizar/', views.perfisView.as_view(), name='Atualizar'),
]
