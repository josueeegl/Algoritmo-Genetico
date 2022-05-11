import numpy as np

def crear_individuos(md = object): #recibimos como parametro el modelo
        #aca se crea un vector dependiendo de los valores, [1,2,5,5]
        individuo = [np.random.randint(md.min, md.max) for i in range(md.rango)] 
        return individuo

def crear_poblacion(md = object): #recibimos como parametro el modelo
        #aca se creara la poblacion de individuos, se crea cada individuo dependiendo el numero que pasemos
        poblacion = [crear_individuos(md) for i in range(md.nIndividuos)] #[[1,2,3], [1,5,5]]
        return poblacion
