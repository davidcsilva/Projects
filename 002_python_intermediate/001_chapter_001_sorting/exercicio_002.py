'''
insertion_sort(
'''


def insertion_sort(lista):
    # Começa do segundo elemento (índice 1), pois o primeiro já é considerado ordenado
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        # Move os elementos maiores que a 'chave' uma posição para a frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        # Insere a 'chave' na sua posição correta
        lista[j + 1] = chave

    return lista


# Exemplo de uso
numeros = [12, 11, 13, 5, 6]
print("Original:", numeros)
print("Ordenado:", insertion_sort(numeros))
