#Metodo de Gauss-Seidel

import numpy as np

def gauss_seidel(A, B, tol=1e-10, max_iter=100):
    n = len(B)
    X = np.zeros_like(B, dtype=np.float64)  # Solução inicial (vetor de zeros)

    for k in range(max_iter):
        X_new = X.copy()

        for i in range(n):
            s1 = sum(A[i][j] * X_new[j] for j in range(i))
            s2 = sum(A[i][j] * X[j] for j in range(i + 1, n))
            X_new[i] = (B[i] - s1 - s2) / A[i][i]

        if np.allclose(X, X_new, atol=tol):
            break
        X = X_new

    return X

# Nova matriz A e vetor B
A = np.array([
    [10, 0, 2, 0, 4],  # Diagonalmente dominante
    [1, 5, 0, 1, 0],
    [0, 1, 4, 0, 0],
    [0, 0, 1, 3, 0],
    [0, 0, 0, 1, 2]
], dtype=float)

B = np.array([30, 45, 35, 15, 4], dtype=float)

# Resolvendo o sistema
X = gauss_seidel(A, B)

# Arredondando para exibir sem casas decimais
X_rounded = np.round(X).astype(int)
print("Solução:", X_rounded)
