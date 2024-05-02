from django.shortcuts import render, redirect
from .forms import NumbEmailForm
from rh.models import Funcionario
from .models import NumbEmail
from datetime import datetime
import re
from django.db.models import DateField
from dateutil.parser import parse
from django.http import QueryDict



def sucesso(request):
    return render(request, 'apps/ti/planilha_emails.html')

from django.db.models import DateField

def banir_numero(request, numero, date_hour):
    # Fazer o parse da string da data e hora para um objeto datetime
    datetime_object = parse(date_hour)

    # Encontrar os objetos NumbEmail com base no número e data/hora e atualizar o status de todos os números para "banido"
    NumbEmail.objects.filter(numero=numero, data=datetime_object).update(status_numb='banido')
    
    # Redirecionar de volta para a URL atual
    return redirect(request.META.get('HTTP_REFERER', 'relatorio_chips'))

def reciclar_numero(request, numero, date_hour):
    # Fazer o parse da string da data e hora para um objeto datetime
    datetime_object = parse(date_hour)

    # Encontrar os objetos NumbEmail com base no número e data/hora e atualizar o status de todos os números para "reciclar"
    NumbEmail.objects.filter(numero=numero, data=datetime_object).update(status_numb='reciclar')
    
    # Redirecionar de volta para a URL atual
    return redirect(request.META.get('HTTP_REFERER', 'relatorio_chips'))

def reciclado_numero(request, numero, date_hour):
    # Fazer o parse da string da data e hora para um objeto datetime
    datetime_object = parse(date_hour)

    # Encontrar os objetos NumbEmail com base no número e data/hora e atualizar o status de todos os números para "reciclado"
    NumbEmail.objects.filter(numero=numero, data=datetime_object).update(status_numb='reciclado')
    
    # Redirecionar de volta para a URL atual
    return redirect(request.META.get('HTTP_REFERER', 'relatorio_chips'))

def excluir_numb(request, numero, date_hour):
    # Fazer o parse da string da data e hora para um objeto datetime
    datetime_object = parse(date_hour)

    # Encontrar e excluir_numb o objeto NumbEmail com base no número e data/hora
    NumbEmail.objects.filter(numero=numero, data=datetime_object).delete()
    
    # Redirecionar de volta para a URL de referência na solicitação
    return redirect(request.META.get('HTTP_REFERER', 'relatorio_chips'))

def excluir_email(request, email, date_hour):
    # Fazer o parse da string da data e hora para um objeto datetime
    datetime_object = parse(date_hour)

    # Encontrar e excluir_email o objeto NumbEmail com base no número e data/hora
    NumbEmail.objects.filter(email=email, data=datetime_object).delete()
    
    # Redirecionar de volta para a URL de referência na solicitação
    return redirect(request.META.get('HTTP_REFERER', 'relatorio_chips'))

def inativar_email(request, email, date_hour):
    # Fazer o parse da string da data e hora para um objeto datetime
    datetime_object = parse(date_hour)

    # Encontrar os objetos NumbEmail com base no número e data/hora e atualizar o status de todos os números para "reciclado"
    NumbEmail.objects.filter(email=email, data=datetime_object).update(status_email='inativo')
    
    # Redirecionar de volta para a URL atual
    return redirect(request.META.get('HTTP_REFERER', 'relatorio_chips'))

def planilha_pass_ip(request):
    return render(request, 'apps/ti/planilha_pass_ip.html')

def planilha_emails(request):
    # Inicialize listas vazias para armazenar os dados que serão exibidos na tabela
    dados_relatorio = []

    # Recupere todos os objetos NumbEmail do banco de dados
    num_emails = NumbEmail.objects.all()
    if request.method == 'GET':
        data_inicio = request.GET.get('data_inicio')
        data_fim = request.GET.get('data_fim')

        if data_inicio and data_fim:
            # Converta as datas de string para objetos datetime
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d')

            num_emails = NumbEmail.objects.filter(data__range=(data_inicio, data_fim))

            # Itere sobre os objetos NumbEmail para processar os dados
            for num_email in num_emails:
                # Inicialize as variáveis gerais como vazias
                cpf = ""
                nome_completo = ""
                setor = ""
                email = ""
                status = ""
                date_hour = ""

                # Verifique se há um email associado (não vazio)
                if num_email.email:
                    # Recupere o funcionário associado ao CPF do objeto NumbEmail
                    try:
                        funcionario = Funcionario.objects.get(cpf=num_email.cpf)
                    except Funcionario.DoesNotExist:
                        funcionario = None

                    # Verifique se o funcionário foi encontrado e está ativo
                    if funcionario and funcionario.status_atividade == 'ativo':
                        # Preencha as variáveis com os dados do funcionário e do objeto NumbEmail
                        cpf = num_email.cpf
                        nome_completo = funcionario.nome_completo
                        setor = funcionario.setor
                        email = num_email.email
                        status = num_email.status_email
                        date_hour = num_email.data

                        # Adicione os dados à lista de dados do relatório
                        dados_relatorio.append({
                            'cpf': cpf,
                            'nome_completo': nome_completo,
                            'setor': setor,
                            'email': email,
                            'status': status,
                            'date_hour': date_hour,
                        })

    # Renderize o template com os dados do relatório
    return render(request, 'apps/ti/planilha_emails.html', {'dados_relatorio': dados_relatorio})

    

def relatorio_chips(request):
    # Inicialize listas vazias para armazenar os dados que serão exibidos na tabela
    dados_relatorio = []

    # Recupere todos os objetos NumbEmail do banco de dados
    num_emails = NumbEmail.objects.all()
    if request.method == 'GET':
        data_inicio = request.GET.get('data_inicio')
        data_fim = request.GET.get('data_fim')

        if data_inicio and data_fim:
            # Converta as datas de string para objetos datetime
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d')

            num_emails = NumbEmail.objects.filter(data__range=(data_inicio, data_fim))

            # Itere sobre os objetos NumbEmail para processar os dados
            for num_email in num_emails:
                # Inicialize as variáveis gerais como vazias
                cpf = ""
                nome_completo = ""
                setor = ""
                operadora_site = ""
                numero = ""
                status = ""
                date_hour = ""

                # Verifique se há um número de telefone associado (não vazio)
                if num_email.numero:
                    # Recupere o funcionário associado ao CPF do objeto NumbEmail
                    try:
                        funcionario = Funcionario.objects.get(cpf=num_email.cpf)
                    except Funcionario.DoesNotExist:
                        funcionario = None

                    # Verifique se o funcionário foi encontrado e está ativo
                    if funcionario and funcionario.status_atividade == 'ativo':
                        # Preencha as variáveis com os dados do funcionário e do objeto NumbEmail
                        cpf = num_email.cpf
                        nome_completo = funcionario.nome_completo
                        setor = funcionario.setor
                        operadora_site = num_email.operadora_site
                        ddd = num_email.ddd
                        numero = num_email.numero
                        status = num_email.status_numb
                        date_hour = num_email.data

                        # Adicione os dados à lista de dados do relatório
                        dados_relatorio.append({
                            'cpf': cpf,
                            'nome_completo': nome_completo,
                            'setor': setor,
                            'operadora_site': operadora_site,
                            'ddd':ddd,
                            'numero': numero,
                            'status': status,
                            'date_hour': date_hour
                        })

    # Renderize o template com os dados do relatório
    return render(request, 'apps/ti/relatorio_chips.html', {'dados_relatorio': dados_relatorio})

def form_addti(request):
    funcionarios = Funcionario.objects.all()
    if request.method == 'POST':
        if 'funcionario' in request.POST:
            cpf_funcionario = request.POST.get('funcionario')
            funcionario = Funcionario.objects.get(cpf=cpf_funcionario)
            operadora_site = ""
            ddd = ""
            numero = ""
            email = ""
            senha_email = ""
            numero_existe = False
            email_existe = False
            sucesso = False
            success_message = f"{numero} salvo no cadastro de {funcionario.nome_completo}"
            if 'numero' in request.POST and request.POST['numero']:
                if 'operadora_site' in request.POST and 'ddd' in request.POST:
                    operadora_site = request.POST['operadora_site']
                    ddd = request.POST['ddd']
                    numero = request.POST['numero']
                    numero_existe = True
                    sucesso = True
                else:
                    error_message = "Por favor, preencha os campos Operadora/Site e DDD antes de salvar."

            if 'email' in request.POST and request.POST['email']:
                if 'senha_email' in request.POST and request.POST['senha_email']:
                    email = request.POST['email']
                    senha_email = request.POST['senha_email']
                    email_existe = True
                    sucesso = True
                else:
                    error_message = "Por favor, preencha o campo Senha antes de salvar."

            if not numero_existe and not email_existe:
                error_message = "Por favor, preencha o número de telefone ou o email antes de salvar."
            else:
                email_numb = NumbEmail.objects.create(
                    cpf=cpf_funcionario,
                    operadora_site=operadora_site,
                    ddd=ddd,
                    numero=numero,
                    email=email,
                    senha_email=senha_email
                )
            if sucesso:
                return render(request, 'apps/rh/list_funcionarios.html', {'success_message': success_message,'funcionarios': funcionarios})
            else:
                return render(request, 'apps/ti/form_addti.html', {'error_message': error_message,'funcionarios': funcionarios})
    else:
        funcionarios = Funcionario.objects.all()
        return render(request, 'apps/ti/form_addti.html', {'funcionarios': funcionarios})
