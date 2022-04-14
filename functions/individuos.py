import numpy as np
import random

class DNA():
    def __init__(self, target, porcentaje, mutacion_rate, nIndividuos, nSelection, nGeneraciones, imprimir = True):
        self.target = target
        self.mutacion_rate = mutacion_rate
        self.nIndividuos = nIndividuos
        self.nSelection = nSelection
        self.nGeneraciones = nGeneraciones
        self.imprimir = imprimir
        self.porcentaje = porcentaje
    

    """ esta funcion es para crear un individuo """
    def crear_individuos(self, min = 0, max = 9): 
        individuos = [np.random.randint(min, max) for i in range(4)]
        return individuos


    """ Se crea la poblacion de 15 individuos """
    def crear_poblacion(self):
        poblacion = [self.crear_individuos() for i in range(self.nIndividuos)]
        return poblacion

    """ se compara cada alelo del target con los del individuo generado """
    def fitnessF(self, individuo):
        fitness = 0
        for i in range(len(individuo)):
            if individuo[i] == self.target:
                fitness += 1    
        return fitness

    """ se selecciona los mejores 5 """
    def seleccion(self, poblacion):
        puntos = [(self.fitnessF(i),i) for i in poblacion]
        puntos = [(i[1]) for i in sorted(puntos)]
        selec = puntos[len(puntos) - self.nSelection :]
        return selec

    def reproduccion_nwGene(self, poblacion, seleccion):
        padre = []

        for i in range(len(poblacion)):
            padre = random.sample(seleccion, 2)

            poblacion[i][:2] = padre[0][:2]
            poblacion[i][2:] = padre[1][2:]
        return  poblacion

    def mutacion(self, poblacion):
        for i in range(len(poblacion)):
            if random.random() <= self.mutacion_rate:
                punto = random.randint(1, 3)
                nuevo_valor = np.random.randint(0 , 9)
                while nuevo_valor == poblacion[i][punto]:
                    nuevo_valor = np.random.randint(0, 9)

                poblacion[i][punto] = nuevo_valor
        return poblacion
        
    def run_AlgoGen(self):
        poblacion = self.crear_poblacion()
        for i in range(self.nGeneraciones):
            if self.imprimir:
                print('_______________')
                print('Generacion: ', i)
                print('Poblacion: ', poblacion)
                
            selec = self.seleccion(poblacion)
            poblacion = self.reproduccion_nwGene(poblacion, selec)
            poblacion = self.mutacion(poblacion)