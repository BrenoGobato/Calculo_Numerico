# Função alvo f(x) = x^2 - 2, cuja raiz corresponde à raiz quadrada de 2
def f(x):
    return x**2 - 2

# Parâmetros iniciais
x0 = 1          # Primeiro valor inicial
x1 = 2          # Segundo valor inicial
tolerance = 1e-6
max_iterations = 1000

# Lista para armazenar detalhes de cada iteração
iterations = []

# Método da secante
for i in range(max_iterations):
    f_x0 = f(x0)
    f_x1 = f(x1)
    # Fórmula do método da secante para o próximo valor
    x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
    
    # Armazena detalhes da iteração atual
    iterations.append((i + 1, x0, x1, x2, f_x0, f_x1, abs(x2 - x1)))

    # Verifica se a precisão desejada foi alcançada
    if abs(x2 - x1) < tolerance:
        break

    # Atualiza os valores para a próxima iteração
    x0, x1 = x1, x2

# Imprime o passo a passo
print("Iteração | x_(n-1)       | x_n           | x_(n+1)       | f(x_(n-1))     | f(x_n)        | |x_(n+1) - x_n|")
for step in iterations:
    print(f"{step[0]:^9}| {step[1]:<13.6f} | {step[2]:<13.6f} | {step[3]:<13.6f} | {step[4]:<13.6f} | {step[5]:<13.6f} | {step[6]:<13.6f}")

# Resultado final
print(f"\nA aproximação final da raiz quadrada de 2 é: {x2}")
