from django.shortcuts import render
from . models import endNum


def muestra_datos(request):
    consulta = endNum.objects.all()
    calculaSuma=suma(consulta)
    contexto = zip(consulta,calculaSuma)
    return render(request, 'listas/index.html',{'contexto':contexto})

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum