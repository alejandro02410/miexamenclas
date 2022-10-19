from django.shortcuts import render
from . models import inicio


def muestra_datos(request):
    consulta = inicio.objects.all()
    calculaSuma=suma(consulta)
    contexto = zip(consulta,calculaSuma)
    return render(request, 'inicio/index1.html',{'contexto':contexto})

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum