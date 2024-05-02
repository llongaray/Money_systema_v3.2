from django.db import models
from rh.models import Funcionario
from datetime import datetime

class Conta(models.Model):
    nome = models.CharField(max_length=20)
    vencimento_dia = models.IntegerField()
    TIPOS_CHOICES = [
        ('GERAL', 'Geral'),
        ('SISTEMA', 'Sistema'),
        ('VOIP', 'Voip'),
    ]
    tipo_conta = models.CharField(max_length=20, choices=TIPOS_CHOICES)

    # SETORES
    Atendimento_POA = models.BooleanField(default=False)
    Atendimento_SM = models.BooleanField(default=False)
    Atendimento_SLE = models.BooleanField(default=False)
    SIAPE = models.BooleanField(default=False)
    INSS = models.BooleanField(default=False)
    TI = models.BooleanField(default=False)
    Marketing = models.BooleanField(default=False)
    Operacional = models.BooleanField(default=False)
    Outros = models.BooleanField(default=False)

    # EMPRESAS
    BOREAL = models.BooleanField(default=False)
    MONEY = models.BooleanField(default=False)
    PARK_GUAIBA = models.BooleanField(default=False)

    # Registro automativo de DATA:HORA
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Gasto(models.Model):
    def comprovante_upload_path(instance, filename):
        now = datetime.now()
        return f'comprovantes/{now.year}{now.month}/{filename}'

    nome_associado = models.CharField(max_length=100)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('Pago', 'Pago'),
        ('A pagar', 'A pagar'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="A pagar")
    comprovante = models.FileField(upload_to=comprovante_upload_path, null=True, blank=True)

    # Registro automativo de DATA:HORA
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome