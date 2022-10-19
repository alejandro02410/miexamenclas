from django.shortcuts import render
from . models import algo1


def muestra_datos(request):
    consulta = algo1.objects.all()
    calculaSuma=suma(consulta)
    contexto = zip(consulta,calculaSuma)
    return render(request, 'algorit1/algoritmo1.html',{'contexto':contexto})

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum