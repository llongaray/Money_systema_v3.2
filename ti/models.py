from django.db import models

class NumbEmail(models.Model):
    cpf = models.CharField(max_length=11)
    email = models.EmailField(blank=True, null=True)
    senha_email = models.CharField(max_length=100, blank=True, null=True)
    operadora_site = models.CharField(max_length=11, blank=True, null=True, default="desconhecido")
    ddd = models.CharField(max_length=2, blank=True, null=True, default="00")
    numero = models.CharField(max_length=9, blank=True, null=True)
    status_numb = models.CharField(max_length=12, blank=True, null=True, default="ativo")
    status_email = models.CharField(max_length=12, blank=True, null=True, default="ativo")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CPF: {self.cpf}, Email: {self.email}, Operadora/Site: {self.operadora_site}, DDD: {self.ddd}, Número: {self.numero}"
