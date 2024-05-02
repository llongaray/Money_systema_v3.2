from django.shortcuts import render, redirect
from .forms import ContaForm, GastoForm
from .models import Conta, Gasto

def form_gastos(request):
    conta_form = ContaForm()
    gasto_form = GastoForm()

    if request.method == 'POST':
        if 'nome' in request.POST:  # Verifica se o formulário de Conta foi submetido
            conta_form = ContaForm(request.POST)
            if conta_form.is_valid():
                conta_form.save()
                # Lógica de redirecionamento ou outras ações após o salvamento da conta
                return redirect('form_gastos')
        elif 'nome_associado' in request.POST:  # Verifica se o formulário de Gasto foi submetido
            gasto_form = GastoForm(request.POST, request.FILES)
            if gasto_form.is_valid():
                gasto_form.save()
                # Lógica de redirecionamento ou outras ações após o salvamento do gasto
                return redirect('form_gastos')
    
    # Obtém todas as contas do banco de dados
    contas = Conta.objects.all()

    context = {
        'conta_form': conta_form,
        'gasto_form': gasto_form,
        'contas': contas,  # Envia as contas para o template
    }
    return render(request, 'apps/financeiro/forms_gastosContas.html', context)



def relat_geral(request):
    pass

def relat_setor(request):
    pass