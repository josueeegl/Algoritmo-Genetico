import numpy as np
import random
from copy import deepcopy
import functions.fitness as fit

def sPadres(poblacion):  # se seleccionan la mitad de los mejores individuos
    for i in range(len(poblacion)):
        poblacion[i].pop(0)
    var = len(poblacion) / 2
    selec = poblacion[:int(var)]
    return selec


def sHijos(p1,  md=object):
    nuevaGen=[]
    hijos = deepcopy(p1)
    mutado = deepcopy(p1)

    if len(p1) % 2 == 1:
        for i in range(int(md.rango / 2)):
            punto = random.randint(1, len(mutado[len(mutado) - 1])-1)
            mutado[len(mutado)-1][punto] = np.random.randint(0, 6)
        p1.append(mutado[len(mutado) - 1])

        hijos.pop(-1)
        nuevaGen = cruce(hijos, md, p1)
    else:
        nuevaGen = cruce(hijos, md, p1)
    return nuevaGen


def cruce(hijos, md=object, p1=[]):
    auxiliar = [hijos[i:i + 2] for i in range(0, len(hijos), 2)]
    for i in range(len(auxiliar)):
        h = [auxiliar[i][j] for j in range(len(auxiliar[i]))]
        h2 = deepcopy(h)
        h[0][int(md.rango / 2):] = h2[1][int(md.rango/2):]
        h[0][:int(md.rango / 2)] = h2[0][:int(md.rango/2)]
        h[1][int(md.rango / 2):] = h2[0][int(md.rango/2):]
        h[1][:int(md.rango / 2)] = h2[1][:int(md.rango/2)]
        p1.append(h[0])
        p1.append(h[1])
    return p1
