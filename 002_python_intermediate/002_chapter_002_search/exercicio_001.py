'''
sequential search
'''


def busca_sequencial(lista, alvo):
    # Percorre a lista elemento por elemento junto com seu índice
    for indice, valor in enumerate(lista):
        # Se encontrar o valor procurado, retorna a posição dele
        if valor == alvo:
            return indice

    # Se percorrer toda a lista e não encontrar, retorna -1
    return -1


# Exemplo de uso
numeros = [15, 8, 42, 4, 23, 16]
procurado = 42

resultado = busca_sequencial(numeros, procurado)

if resultado != -1:
    print(f"Elemento {procurado} encontrado no índice {resultado}.")
else:
    print(f"Elemento {procurado} não encontrado na lista.")
