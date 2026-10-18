'''
Escreva um programa que calcule a raiz quadrada de um número.
Utilize o método de Newton para obter um resultado aproximado. Sendo n o nú-
mero a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula
p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule
p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o
quadrado de p for menor que 0,0001.
'''

# Leitura do número
n = float(input("Digite um número para calcular a raiz quadrada: "))

if n < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo no conjunto dos números reais.")
elif n == 0:
    print("A raiz quadrada de 0 é 0.0")
else:
    # Valor inicial da base b
    b = 2.0
    p = (b + (n / b)) / 2.0

    # O ciclo repete-se enquanto a diferença absoluta entre n e p² for >= 0.0001
    while abs(n - (p ** 2)) >= 0.0001:
        b = p
        p = (b + (n / b)) / 2.0

    print(f"\nA raiz quadrada aproximada de {n} é: {p:.5f}")
    print(f"Verificação: {p:.5f}² = {p**2:.5f}")
