'''
Bubblesort
'''


def bubble_sort(lista):
    n = len(lista)

    # Percorre todos os elementos da lista
    for i in range(n):
        trocou = False

        # Os últimos 'i' elementos já estão ordenados
        for j in range(0, n - i - 1):
            # Compara o elemento atual com o próximo
            if lista[j] > lista[j + 1]:
                # Troca os elementos de lugar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True

        # Se nenhuma troca foi feita nessa passagem, a lista já está ordenada
        if not trocou:
            break

    return lista


# Exemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numeros)
print("Ordenado:", bubble_sort(numeros))
