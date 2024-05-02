from django.shortcuts import render, redirect
from .forms import FuncionarioForm
from .models import Funcionario
from decimal import Decimal
import holidays
from datetime import date

def get_dias_uteis_mes_atual():
    # Obtendo os feriados nacionais do Brasil
    cal = holidays.Brazil()

    # Obtendo o mês e o ano atual
    today = date.today()
    year = today.year
    month = today.month

    # Contagem dos dias úteis
    dias_uteis = 0

    # Iterando sobre cada dia do mês atual
    for day in range(1, 32):
        try:
            # Verificando se o dia é útil (não é sábado, domingo ou feriado)
            current_date = date(year, month, day)
            if current_date.weekday() < 5 and current_date not in cal:
                dias_uteis += 1
        except ValueError:
            # Se houver um erro ao criar a data, significa que ultrapassamos o último dia do mês
            break

    return dias_uteis

def list_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    for funcionario in funcionarios:
        # Define as variáveis de acordo com as instruções
        funcionario.nome = funcionario.nome_completo
        funcionario.cpf = funcionario.cpf
        funcionario.tipo_contrato = funcionario.tipo_contrato
        funcionario.cnpj = funcionario.cnpj
        funcionario.chip_assoc = '--/--'
        funcionario.emails_assoc = '--/--'
        funcionario.status_vr = 'Utilizando' if funcionario.vr_ativo else 'Não utilizando'
        funcionario.status_vt = 'Utilizando' if funcionario.vt_ativo else 'Não utilizando'
    return render(request, 'apps/rh/list_funcionarios.html', {'funcionarios': funcionarios})


def list_salarios(request):
    funcionarios = Funcionario.objects.all()
    for funcionario in funcionarios:
        funcionario.salario_bruto = funcionario.salario
        if funcionario.tipo_contrato.lower() == 'clt':
            # Desconto de 8% para FGTS
            fgts_percentual = Decimal('0.08')
            funcionario.fgts = funcionario.salario_bruto * fgts_percentual
            
            # Desconto de INSS conforme a tabela
            salario_contribuicao = funcionario.salario_bruto
            if salario_contribuicao <= 1412:
                inss_percentual = Decimal('0.075')
            elif salario_contribuicao <= 2666.68:
                inss_percentual = Decimal('0.09') 
            elif salario_contribuicao <= 4000.03:
                inss_percentual = Decimal('0.12')
            else:
                inss_percentual = Decimal('0.14')
            inss = salario_contribuicao * inss_percentual
            inss = min(inss, Decimal('181.18'))
            
            # Desconto de 20% sobre o valor do vale-alimentação (VR)
            vr_diario = funcionario.vr_valor_diario if funcionario.vr_ativo else Decimal('0')
            vr_mensal = vr_diario * get_dias_uteis_mes_atual()
            desconto_vr = vr_mensal * Decimal('0.20')
            
            # Desconto de 6% sobre o salário bruto para o vale transporte (VT)
            desconto_vt = funcionario.salario_bruto * Decimal('0.055')

            # Total de descontos
            total_descontos = inss + desconto_vr + desconto_vt
            
            # Cálculo do salário líquido
            funcionario.descontos = total_descontos
            funcionario.valor_liquido = funcionario.salario_bruto - total_descontos
        elif funcionario.tipo_contrato.lower() == 'estágio':
            # Se for estágio, não há descontos
            funcionario.fgts = Decimal('0')
            funcionario.descontos = Decimal('0')
            funcionario.valor_liquido = funcionario.salario_bruto
        else:
            # Se não for CLT ou estágio, não há descontos
            funcionario.fgts = Decimal('0')
            funcionario.descontos = Decimal('0')
            funcionario.valor_liquido = funcionario.salario_bruto
    return render(request, 'apps/rh/list_salarios.html', {'funcionarios': funcionarios})


def list_beneficios(request):
    funcionarios = Funcionario.objects.all()
    for funcionario in funcionarios:
        if funcionario.tipo_contrato.lower() == 'clt' or funcionario.tipo_contrato.lower() == 'estágio':
            # Se for CLT ou estágio, calcula os benefícios
            vr_diario = funcionario.vr_valor_diario if funcionario.vr_ativo else Decimal('0')
            vt_diario = funcionario.vt_valor_diario if funcionario.vt_ativo else Decimal('0')
            dias_uteis_mes = get_dias_uteis_mes_atual()
            vr_mensal = vr_diario * dias_uteis_mes
            vt_mensal = vt_diario * dias_uteis_mes
            total_beneficios = vr_mensal + vt_mensal

            # Define as variáveis para os campos específicos
            funcionario.vr_diario = vr_diario
            funcionario.vr_mensal = vr_mensal
            funcionario.vt_diario = vt_diario
            funcionario.vt_mensal = vt_mensal
            funcionario.dias_uteis_mes = dias_uteis_mes  # Adicionando dias úteis aqui
            funcionario.total_beneficios = total_beneficios
        else:
            # Se não for CLT ou estágio, não há benefícios
            funcionario.vr_diario = Decimal('0')
            funcionario.vr_mensal = Decimal('0')
            funcionario.vt_diario = Decimal('0')
            funcionario.vt_mensal = Decimal('0')
            funcionario.dias_uteis_mes = Decimal('0')
            funcionario.total_beneficios = Decimal('0')

    return render(request, 'apps/rh/list_beneficios.html', {'funcionarios': funcionarios})


def form_funcionarios(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'apps/rh/form_funcionarios.html', {'form': form})