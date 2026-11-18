'''
quicksort
'''


def quick_sort(lista):
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas
    if len(lista) <= 1:
        return lista

    # Escolhe o elemento central como pivô (ajuda a evitar o pior caso em listas já ordenadas)
    pivo = lista[len(lista) // 2]

    # Particiona os elementos em três sublistas
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    # Ordena recursivamente as sublistas e concatena o resultado
    return quick_sort(menores) + iguais + quick_sort(maiores)


# Exemplo de uso
numeros = [10, 7, 8, 9, 1, 5]
print("Original:", numeros)
print("Ordenado:", quick_sort(numeros))
