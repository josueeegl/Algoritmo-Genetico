import numpy as np
import random
import functions.individuos as indiv



def main():
    target = [2,2,2,2,2,2,2]
    model = indiv.DNA(target=target, mutacion_rate = 0.2, nIndividuos = 25, nSelection = 5, nGeneraciones=50, imprimir=True)
    model.run_AlgoGen()

if __name__ == '__main__':
    main()