from django.urls import path
from .views import list_funcionarios, list_salarios, list_beneficios, form_funcionarios

urlpatterns = [
    path('funcionarios/', list_funcionarios, name="list_funcionarios"),
    path('salarios/', list_salarios, name="list_salarios"),
    path('beneficios/', list_beneficios, name="list_beneficios"),
    path('cadastrar_funcionario/', form_funcionarios, name="form_funcionarios"),
]
