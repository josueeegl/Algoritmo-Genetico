from flask import jsonify
import alGenets as al
import json


def respuesta():
    valor = al.algoritmo(convergencia=0.90, target=5, nVacunas=2,
                         nContagios=1, nIndividuos=8, rango=8, max=6, min=0)

    lis = []
    lista3 = {}
    i = 0
    datos = {'generacion': valor[0], 'convergencia': valor[1]}

    for element in valor[2]:  # es una opcion
        for el in element:
            elementData2 = json.dumps(el)
            lis.append(elementData2)
        lista3['generacion' + str(i)] = lis
        i += 1
        lis = []

    return jsonify({'generaciones': lista3, 'datosfinales': datos})


def respuesta2(convergencia, target, nVacunas, nContagios, nIndividuos, rango, max, min):
    valor = al.algoritmo(float(convergencia), int(target), int(nVacunas),
                         int(nContagios), int(nIndividuos), int(rango), int(max), int(min))
    lis = []
    lista3 = {}
    i = 0
    datos = {'generacion': valor[0], 'convergencia': valor[1]}

    for element in valor[2]:  # es una opcion
        for el in element:
            elementData2 = (el)
            lis.append(elementData2)
        lista3['generacion ' + str(i)] = lis
        i += 1
        lis = []
    
    return jsonify({'generaciones': lista3, 'datosfinales': datos})
