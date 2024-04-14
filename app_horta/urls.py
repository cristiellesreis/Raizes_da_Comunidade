from django.urls import path
from app_horta.views import criar_horta, minha_horta, inserir_cultura

urlpatterns = [
    path('horta/', minha_horta, name='minha_horta'),
    path('horta/criar', criar_horta, name='criar_horta'),
    path('horta/inserir/', inserir_cultura, name='inserir_cultura')
]