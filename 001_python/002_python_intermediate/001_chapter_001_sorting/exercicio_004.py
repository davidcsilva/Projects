'''
shellsort
'''


def shell_sort(lista):
    n = len(lista)
    # Começa com um gap grande e vai diminuindo
    gap = n // 2

    while gap > 0:
        # Faz um insertion sort com o gap atual
        for i in range(gap, n):
            temp = lista[i]
            j = i

            # Move os elementos para a direita se forem maiores que o temp
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap

            # Insere o temp na posição correta
            lista[j] = temp

        # Diminui o gap
        gap //= 2

    return lista


# Exemplo de uso
numeros = [12, 34, 54, 2, 3]
print("Original:", numeros)
print("Ordenado:", shell_sort(numeros))
