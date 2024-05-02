from django.urls import path
from .views import relatorio_chips, planilha_pass_ip, inativar_email, planilha_emails, form_addti, banir_numero, reciclar_numero, reciclado_numero, excluir_numb, excluir_email

urlpatterns = [
    path('form_addti/', form_addti, name="form_addti"),
    path('relatorio_chips/', relatorio_chips, name="relatorio_chips"),
    path('planilha_pass_ip/', planilha_pass_ip, name="planilha_pass_ip"),
    path('planilha_emails/', planilha_emails, name="planilha_emails"),
    path('banir_numero/<str:numero>/<str:date_hour>/', banir_numero, name='banir_numero'),
    path('reciclar_numero/<str:numero>/<str:date_hour>/', reciclar_numero, name='reciclar_numero'),
    path('reciclado_numero/<str:numero>/<str:date_hour>/', reciclado_numero, name='reciclado_numero'),
    path('excluir_numb/<str:numero>/<str:date_hour>/', excluir_numb, name='excluir_numb'),
    path('inativar_email/<str:email>/<str:date_hour>/', inativar_email, name='inativar_email'),
    path('excluir_email/<str:email>/<str:date_hour>/', excluir_email, name='excluir_email'),
]
