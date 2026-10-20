'''
Altere o programa da listagem 6.33 de forma a imprimir o menor
elemento da lista.
'''


L = [15, 7, 27, 39, 12, 7, 80, 27, 15]

# Inicializa a variável 'menor' com o primeiro elemento da lista
menor = L[0]

x = 1  # Começa do segundo elemento
while x < len(L):
    if L[x] < menor:
        menor = L[x]  # Atualiza se encontrar um valor menor
    x += 1

print(f"O menor elemento da lista é: {menor}")
