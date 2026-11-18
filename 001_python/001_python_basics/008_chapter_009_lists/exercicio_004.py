'''
Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x
'''

string = input("String: ")

contagem = {}

# Contagem das ocorrências de cada caractere
for caractere in string:
    contagem[caractere] = contagem.get(caractere, 0) + 1

print("\nResultado:")
# Exibição no formato solicitado (Caractere: Nx)
for caractere, quantidade in contagem.items():
    print(f"{caractere}: {quantidade}x")
