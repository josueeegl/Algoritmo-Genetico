import numpy as np
import random

class DNA():
    def __init__(self, fitness, mutacion_rate, nIndividuos, nSelection, nGeneraciones, imprimir = True):
        self.fitness = fitness
        self.mutacion_rate = mutacion_rate
        self.nIndividuos = nIndividuos
        self.nSelection = nSelection
        self.nGeneraciones = nGeneraciones
    

    """ esta funcion es para crear un individuo """
    def crear_individuos(self, min = 0, max = 9): 
        individuos = [np.random.randint(min, max) for i in range(len(self.fitness))]
        return individuos


    """ Se crea la poblacion de 15 individuos """
    def crear_poblacion(self):
        poblacion = [self.crear_individuos() for i in range(self.nIndividuos)]
        print(poblacion)

def main():
    fitness = [1,0,0,1,0,1.1]
    model = DNA(fitness=fitness, mutacion_rate = 0.02, nIndividuos = 15, nSelection = 5, nGeneraciones=50, imprimir=False)
    model.crear_poblacion()

if __name__ == '__main__':
    main()