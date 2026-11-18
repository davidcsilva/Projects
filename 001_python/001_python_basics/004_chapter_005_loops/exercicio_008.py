'''
Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a mul-
tiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
'''

# Leitura dos dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Identifica os valores absolutos (módulos) sem usar a função abs()
a = num1 if num1 >= 0 else -num1
b = num2 if num2 >= 0 else -num2

# Multiplicação por somas sucessivas
resultado_abs = 0
for _ in range(a):
    resultado_abs += b

# Define o sinal do resultado final
# Se um (e apenas um) dos números for negativo, o resultado é negativo
if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    resultado = -resultado_abs
else:
    resultado = resultado_abs

print(f"O resultado de {num1} x {num2} é: {resultado}")
