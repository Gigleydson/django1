from django.shortcuts import render


def index(request):
    print(dir(request.user))
    print(f'User: {request.user}')

    if str(request.user) == 'AnonymousUser':
        user = 'Usuário não logado'
    else:
        user = 'Usuário logado'

    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é muito foda!',
        'logado': user,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
