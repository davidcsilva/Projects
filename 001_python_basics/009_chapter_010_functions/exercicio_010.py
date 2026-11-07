'''
Reescreva a função para cálculo da sequência de Fibonacci, sem
utilizar recursão.

'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



print(fibonacci(0))  # Retorna 0
print(fibonacci(1))  # Retorna 1
print(fibonacci(2))  # Retorna 1
print(fibonacci(6))  # Retorna 8
print(fibonacci(10)) # Retorna 55
