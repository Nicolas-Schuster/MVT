from django.shortcuts import render
from django.http import HttpResponse
from MVT.models import Famillia



def crear_familliar(request):
    Famillia.objects.create(name= 'silvana', edad=48, vive=True)
    return HttpResponse('nuevo familliar')

def list_famillia(request):
    all_famillia = Famillia.objects.all
    context ={
        'famillia':all_famillia,
    }
    return render(request, 'list_famillia.html', context=context)