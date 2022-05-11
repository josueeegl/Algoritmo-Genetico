from operator import itemgetter
import functions.imprimir as imp

def fitnessF(poblacion, md=object):
    fitness = 0
    suma = 0
    print('Población inicial: \n')
    imp.imprimir(poblacion)
    print('\nIndividuos son su valor fitness: \n')

    for i in range(len(poblacion)): #recorremos la poblacion
        for j in range(len(poblacion[i])): #recorremos el individuo
            aux = poblacion[i][j] #se guardar el valor en una variable
            if aux == md.target: #si el valor es mayor o igual al target(ya es inmune)
                fitness += md.target
            elif aux >= md.nVacunas: # si el vlaor el mayor o igual al numero de vacunas(se ha vacunado con las correspondientes)
                fitness += md.nVacunas
            elif aux >= md.nContagios: #si se contagiado mas de una vez
                fitness += md.nContagios

        poblacion[i].insert(0,fitness) #se agrega el fitness al final del individuo
        print(poblacion[i], ' = ' + str(fitness))
        suma += fitness
        fitness = 0
    print('\n------------------------\n')
    print('Suma de valores fitness de la poblacion: ',suma)
    pobOrdenada = ordenar(poblacion)
    return [pobOrdenada, suma]

def ordenar(poblacion):
    orden = sorted(poblacion, key=itemgetter(0), reverse=True)
    return orden

