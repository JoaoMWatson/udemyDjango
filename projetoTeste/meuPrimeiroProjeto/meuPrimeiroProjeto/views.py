from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse(f'o ano passado foi:{str(year)}')

def lerDoBanco(nome):
    list_nomes = [
        {'nome': 'ana', 'idade':20},
        {'nome': 'Pedro', 'idade':25},
        {'nome': 'Joaquim', 'idade':29}
    ]

    for pessoa in list_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Nao encontrado', 'idade':0}


def fname(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse(f"Nome:{result['nome']} Idade:{result['idade']}")
    else:
        return HttpResponse('Nao encontrada')


def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade':idade})