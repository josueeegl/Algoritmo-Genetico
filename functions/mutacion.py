import numpy as np
import random


def mutar(p1):
    for i in range(int(len(p1) / 2), len(p1)):
        punto = random.randint(0, len(p1[i]) - 1)
        nuevo_valor = np.random.randint(0, 6)
        while nuevo_valor == p1[i][punto]:
            nuevo_valor = np.random.randint(0, 6)
        p1[i][punto] = nuevo_valor
    return p1
