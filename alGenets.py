import functions.fitness as fit
import functions.variables as var
import functions.poblacion as pob
import functions.seleccion as sele
import functions.mutacion as mut
import functions.imprimir as imp
# mode lo de datos


def finalizacion(md=object):
    valor = 0
    for i in range(md.nIndividuos):
        for i in range(md.rango):
            valor += md.target
    return valor


def algoritmo(convergencia, target, nVacunas, nContagios, nIndividuos, rango, max, min):
    listageneraciones = []
    md = var.md_genetycs(convergencia, target, nVacunas,
                         nContagios, nIndividuos, rango, max, min)
    pob_inicial = pob.crear_poblacion(md)
    valores = fit.fitnessF(pob_inicial, md)
    padres = sele.sPadres(valores[0])
    nueva_gen = sele.sHijos(padres, md)
    mutado = mut.mutar(nueva_gen)

    total = finalizacion(md)
    convergencia = valores[1] / total
    print(total)
    i = 1
    listageneraciones.append(pob_inicial)

    while convergencia < md.convergencia:

        x = fit.fitnessF(mutado, md)
        p = sele.sPadres(x[0])
        nueva_gen = (sele.sHijos(p, md))
        mutado = mut.mutar(nueva_gen)
        convergencia = x[1] / total
        listageneraciones.append(mutado)
        i += 1
    return [i-1, (convergencia*100), listageneraciones, mutado]
