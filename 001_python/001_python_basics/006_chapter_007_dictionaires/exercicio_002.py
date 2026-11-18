'''
Escreva um programa que gere um dicionário, onde cada chave seja
um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}
'''

frase = input("Digite uma frase: ")

contagem = {}

for caractere in frase:
    # Incrementa o valor se a chave já existir, ou inicializa com 1 se for nova
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1

print(contagem)
