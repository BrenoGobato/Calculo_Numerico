#Comando np.linalg.solve

import numpy as np

A = np.array([[5,0,2,0,4], [1,2,0,1,0], [0,1,1,0,0], [0,0,1,1,0], [0,0,0,1,1]])
B = np.array([25,20,15,10,5])

# Resolvendo o sistema
X = np.linalg.solve(A, B)
lista = []
for i in range(len(X)):
    lista.append(round(X[i]))

print(lista)
