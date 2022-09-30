from django.shortcuts import render
from . models import endNum


def muestra_datos(request):
    consulta = endNum.objects.all()
    contexto = {'data': consulta}
    return render(request, 'listas/index.html',contexto)

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum