import numpy as np
import random
import functions.individuos as indiv

def main():
    model = indiv.DNA(target=2,porcentaje=0.9, mutacion_rate = 0.2, nIndividuos = 4, nSelection = 5, nGeneraciones=50, imprimir=True)
    model.run_AlgoGen()

if __name__ == '__main__':
    main()