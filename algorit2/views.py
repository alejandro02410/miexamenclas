from django.shortcuts import render
from . models import algo2


def muestra_datos(request):
    consulta = algo2.objects.all()
    calculaSuma=suma(consulta)
    contexto = zip(consulta,calculaSuma)
    return render(request, 'algorit2/algoritmo2.html',{'contexto':contexto})

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum