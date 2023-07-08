from django.urls import path
from . import views

urlpatterns = [
    path('novo_valor/', views.novo_valor, name='novo_valor'),
    path('view_extrato/', views.extrato, mame='view_extrato'),
]
