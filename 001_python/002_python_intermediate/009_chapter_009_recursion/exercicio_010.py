'''
Algoritmo recursivo para o MergeSort (Ordenação por Intercalação).

O MergeSort segue o paradigma de Divisão e Conquista:
1. Divisão: divide a lista recursivamente pela metade até sublistas de 0 ou 1 elemento (caso base).
2. Conquista / Intercalação (Merge): combina duas metades já ordenadas em uma lista ordenada única.

Complexidade de Tempo: O(n log n) no melhor, médio e pior caso.
Complexidade de Espaço: O(n) auxiliar.
'''


def intercalar(esquerda: list[int], direita: list[int]) -> list[int]:
    """Combina (intercala) duas listas previamente ordenadas em uma única lista ordenada."""
    resultado: list[int] = []
    i = j = 0

    # Compara elementos de ambas as listas e insere o menor no resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes de qualquer uma das metades
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def mergesort(lista: list[int]) -> list[int]:
    """Ordena uma lista de inteiros utilizando o algoritmo MergeSort recursivo."""
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas
    if len(lista) <= 1:
        return lista

    # 1. Divisão: encontra o ponto médio e divide a lista
    meio = len(lista) // 2
    metade_esquerda = mergesort(lista[:meio])
    metade_direita = mergesort(lista[meio:])

    # 2. Conquista: intercala as duas metades ordenadas
    return intercalar(metade_esquerda, metade_direita)


if __name__ == "__main__":
    lista_original = [38, 27, 43, 3, 9, 82, 10, -5, 0, 15]
    lista_ordenada = mergesort(lista_original)

    print("=== Demonstração do MergeSort ===")
    print(f"Lista original: {lista_original}")
    print(f"Lista ordenada: {lista_ordenada}")

    # Testes com casos especiais
    print(f"\nLista vazia:    {mergesort([])}")
    print(f"Um elemento:    {mergesort([42])}")
    print(f"Já ordenada:    {mergesort([1, 2, 3, 4, 5])}")
    print(f"Decrescente:    {mergesort([5, 4, 3, 2, 1])}")
