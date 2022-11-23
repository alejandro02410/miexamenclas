from django.shortcuts import render
from . models import algo1
import math
import random

def muestra_datos(request):
    x1 = random.randint(1,500)
    x2 = random.randint(1,500)
    x3 = random.randint(1,500)
    k = random.randint(0,150)
    df = algo1.objects.all()

    ldis = distanciaEu(df,x1,x2,x3,k)
    repetidas = cuentaVecino(df,k)
    contexto = zip(df,ldis,repetidas)

    return render(request, 'algorit1/algoritmo1.html',{'contexto':contexto})


def distanciaEu(df,x1,x2,x3,k):
    ldist = []
    for i in df:
        dis = (x1 - i.x1)**2+(x2 - i.x3)**2+(x3 - i.x4)**2
        raiz = round(math.sqrt(dis),4)
        ldist.append(raiz)
    
    return ldist

def cuentaVecino(df,k):
    lista=[]
    repetidas = []
    for i in df:
        #rellena la lista con la base de datos
        lista.append(i.x2)
    auxiliar =0
    letra = ""
    for j in range(k):
        if lista[j]==lista[auxiliar]:
            letra = lista[j]
            
        auxiliar+=1
    return letra
        
    
    


    