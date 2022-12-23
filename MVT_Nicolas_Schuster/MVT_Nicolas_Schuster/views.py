from django.http import HttpResponse
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse('Hola mundo')


def madre(request):
    context = {
        'nombre':'silvana',
        'edad': 48,
        'vive': True,
        'lista_gustos': ['bailar', 'salir a caminar', 'escuchar musica']
    }
    return render(request, 'madre.html', context=context)

