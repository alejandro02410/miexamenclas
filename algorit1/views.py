from django.shortcuts import render
from . models import algo1
import math
import random

def muestra_datos(request):
    x1 = random.randint(1,500)
    x2 = random.randint(1,500)
    x3 = random.randint(1,500)
    df = algo1.objects.all()

    ldis = distanciaEu(df,x1,x2,x3)
    ldis = sorted(ldis)
    contexto = zip(df,ldis)

    return render(request, 'algorit1/algoritmo1.html',{'contexto':contexto})


def distanciaEu(df,x1,x2,x3):

    ldist = []

    for i in df:

        dis = (x1 - i.x1)**2+(x2 - i.x3)**2+(x3 - i.x4)**2
        raiz = round(math.sqrt(dis),4)
        ldist.append(raiz)

    return ldist