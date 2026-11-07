'''
Escreva um programa que calcule o resto da divisão inteira entre dois
números. Utilize apenas as operações de soma e subtração para calcular o resultado.
'''

# Leitura dos dois números inteiros
dividendo = int(input("Digite o dividendo (primeiro número): "))
divisor = int(input("Digite o divisor (segundo número): "))

if divisor == 0:
    print("Erro: Não é possível dividir por zero!")
else:
    # Obter os valores absolutos usando apenas comparações
    a = dividendo if dividendo >= 0 else -dividendo
    b = divisor if divisor >= 0 else -divisor

    resto_abs = a

    # Subtrações sucessivas até que o resto seja menor que o divisor
    while resto_abs >= b:
        resto_abs -= b

    # O resto acompanha o sinal do dividendo
    resto = -resto_abs if dividendo < 0 else resto_abs

    print(f"\nO resto da divisão de {dividendo} por {divisor} é: {resto}")
