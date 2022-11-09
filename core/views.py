from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é muito foda!',
        'git': 'Teste de commit',
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
