from django.urls import path
from .views import index, relatorio_geral

urlpatterns = [
    path('', index, name="index"),
    path('relatorio_geral/', relatorio_geral, name="relatorio_geral")
]
