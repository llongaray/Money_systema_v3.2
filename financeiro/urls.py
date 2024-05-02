from django.urls import path
from .views import form_gastos, relat_geral, relat_setor

urlpatterns = [
    path('form_gastos/', form_gastos, name="form_gastos"),
    path('relat_geral/', relat_geral, name="relat_geral"),
    path('relat_setor/', relat_setor, name="relat_setor"),
]
