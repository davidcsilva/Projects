'''
selection_sort
'''


def selection_sort(lista):
    # Percorre todos os elementos da lista
    for i in range(len(lista)):
        # Encontra o índice do menor elemento na parte não ordenada
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j

        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

    return lista


# Exemplo de uso
numeros = [64, 25, 12, 22, 11]
print("Original:", numeros)
print("Ordenado:", selection_sort(numeros))
