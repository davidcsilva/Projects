'''
Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
Exemplos: 454, 10501
'''

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print(
        f"O número {numero} NÃO é palíndromo (números negativos não são palíndromos).")
else:
    original = numero
    invertido = 0

    # Processo de inversão matemática dos dígitos
    while numero > 0:
        ultimo_digito = numero % 10
        invertido = (invertido * 10) + ultimo_digito
        numero = numero // 10

    if original == invertido:
        print(f"O número {original} É PALÍNDROMO.")
    else:
        print(f"O número {original} NÃO é palíndromo.")
