from django.shortcuts import render
from . models import algo3
from django.http import HttpResponse
import numpy as np

def regresionLog(request):
    return render(request, 'algorit3/algoritmo3.html')

def interpretar(request):
    if request.GET["x1"].isdigit() and request.GET["x2"].isdigit():
        x1 = int(request.GET["x1"])
        x2 = int(request.GET["x2"])
        datos = algo3.objects.all()
        b = calcConstante(datos)
        resultado  = valorReferente(datos, x1, x2, b)
        return render(request, 'algorit3/algoritmo3.html', {'consulta': resultado} )
    else:
        mensaje = "Te falto llenar o llenaste incorrectamente, recuerda que deben ser valores numericos"
    return HttpResponse(mensaje)

def valorReferente(datos, x1, x2, b):
    a1 = 0
    a2 = 0
    caracter = ''
    for i in datos:
        a1 = i.x1
        caracter = i.x2
        a2 = i.x3
        break
    salida = 1/(1 + np.exp(-(a1*x1 + a2*x2 + b)))
    if salida > 0.5:
        respuesta = f'El caracter obtenido es: {caracter}'
    else:
        respuesta = f'No hay caracter que haya podido encontrar: {caracter}'
    return respuesta

def calcConstante(datos):
    x = []
    y = []
    xCuadrada = 0
    xy = 0
    for i in datos:
        xCuadrada = xCuadrada + i.x1**2
        xy = xy + i.x1 * i .x3
        x.append(i.x1)
        y.append(i.x3)
    xSum = sum(x)
    ySum = sum(y)
    constante = (xCuadrada*ySum - xy*xSum)/(datos.count()*xCuadrada-xSum**2)
    return constante