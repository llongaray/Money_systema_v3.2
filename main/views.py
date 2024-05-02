from django.shortcuts import render

def index(request):
    return render(request, 'apps/main/welcome.html')

def relatorio_geral(request):
    return render(request, 'apps/main/relatorio_geral.html')