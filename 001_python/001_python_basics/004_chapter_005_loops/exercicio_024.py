'''
Modifique o programa anterior de forma a ler um número n. Imprima
os n primeiros números primos.
'''

# Leitura da quantidade de números primos
n = int(input("Digite a quantidade de números primos que deseja exibir: "))

quantidade_encontrada = 0
numero = 2  # Primeiro número a ser testado

print(f"\nOs primeiros {n} números primos são:")

while quantidade_encontrada < n:
    # Verificação se o 'numero' atual é primo
    if numero == 2:
        e_primo = True
    elif numero % 2 == 0:
        e_primo = False
    else:
        e_primo = True
        divisor = 3
        while divisor < numero:
            if numero % divisor == 0:
                e_primo = False
                break
            divisor += 2

    # Se for primo, exibe e incrementa o contador de primos encontrados
    if e_primo:
        print(numero, end=" ")
        quantidade_encontrada += 1

    numero += 1

print()  # Quebra de linha ao final
