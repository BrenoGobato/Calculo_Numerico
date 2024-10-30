import numpy as np

def jacobi(A, B, tol=1e-2, max_iter=100):
    n = len(B)
    X = np.zeros_like(B, dtype=np.float64)  # Solução inicial (vetor de zeros)
    X_new = np.zeros_like(X)

    for k in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * X[j] for j in range(n) if j != i)
            X_new[i] = (B[i] - s) / A[i][i]

        if np.allclose(X, X_new, atol=tol):
            break
        X = X_new.copy()

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
X = jacobi(A, B)

# Arredondando para exibir sem casas decimais
X_rounded = np.round(X).astype(int)
print("Solução:", X_rounded)
