# Generated by Django 5.0.3 on 2024-05-02 16:54

import financeiro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('vencimento_dia', models.IntegerField()),
                ('tipo_conta', models.CharField(choices=[('GERAL', 'Geral'), ('SISTEMA', 'Sistema'), ('VOIP', 'Voip')], max_length=20)),
                ('Atendimento_POA', models.BooleanField(default=False)),
                ('Atendimento_SM', models.BooleanField(default=False)),
                ('Atendimento_SLE', models.BooleanField(default=False)),
                ('SIAPE', models.BooleanField(default=False)),
                ('INSS', models.BooleanField(default=False)),
                ('TI', models.BooleanField(default=False)),
                ('Marketing', models.BooleanField(default=False)),
                ('Operacional', models.BooleanField(default=False)),
                ('Outros', models.BooleanField(default=False)),
                ('BOREAL', models.BooleanField(default=False)),
                ('MONEY', models.BooleanField(default=False)),
                ('PARK_GUAIBA', models.BooleanField(default=False)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_associado', models.CharField(max_length=100)),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Pago', 'Pago'), ('A pagar', 'A pagar')], default='A pagar', max_length=20)),
                ('comprovante', models.FileField(blank=True, null=True, upload_to=financeiro.models.Gasto.comprovante_upload_path)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]