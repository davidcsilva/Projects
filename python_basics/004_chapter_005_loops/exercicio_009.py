'''
Escreva um programa que leia dois números. Imprima a divisão
inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender o quociente da divisão de dois números como a quantidade
de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez
que podemos subtrair 4 cinco vezes de 20.
'''

# Leitura dos dois números inteiros
dividendo = int(input("Digite o dividendo (primeiro número): "))
divisor = int(input("Digite o divisor (segundo número): "))

if divisor == 0:
    print("Erro: Não é possível dividir por zero!")
else:
    # Obter os valores absolutos sem usar a função abs()
    a = dividendo if dividendo >= 0 else -dividendo
    b = divisor if divisor >= 0 else -divisor

    quociente_abs = 0
    resto_abs = a

    # Subtrações sucessivas
    while resto_abs >= b:
        resto_abs -= b
        quociente_abs += 1

    # Ajuste dos sinais para o quociente e resto
    # Quociente é negativo se apenas um dos números for negativo
    if (dividendo < 0 and divisor > 0) or (dividendo > 0 and divisor < 0):
        quociente = -quociente_abs
    else:
        quociente = quociente_abs

    # No algoritmo de divisão inteira padrão em Python, o resto acompanha o sinal do dividendo
    resto = -resto_abs if dividendo < 0 else resto_abs

    print(f"\nResultado da divisão de {dividendo} por {divisor}:")
    print(f"Quociente (divisão inteira): {quociente}")
    print(f"Resto da divisão: {resto}")
