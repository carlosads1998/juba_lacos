from django.urls import path
from . import views

app_name= 'perfil'

urlpatterns = [
    path('', views.Criar.as_view(), name='Criar'),
    path('atualizar/', views.Atualizar.as_view(), name='Atualizar'),
    path('login', views.Login.as_view(), name='Login'),
    path('logout', views.Logout.as_view(), name='Logout'),
]
