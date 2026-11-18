'''
merge ou interleaving
'''


def merge_vetores(vetor1, vetor2):
    resultado = []
    i = 0  # Ponteiro para o vetor1
    j = 0  # Ponteiro para o vetor2

    # Compara os elementos de ambos os vetores e adiciona o menor ao resultado
    while i < len(vetor1) and j < len(vetor2):
        if vetor1[i] <= vetor2[j]:
            resultado.append(vetor1[i])
            i += 1
        else:
            resultado.append(vetor2[j])
            j += 1

    # Adiciona os elementos restantes do vetor1 (se houver)
    while i < len(vetor1):
        resultado.append(vetor1[i])
        i += 1

    # Adiciona os elementos restantes do vetor2 (se houver)
    while j < len(vetor2):
        resultado.append(vetor2[j])
        j += 1

    return resultado


# Exemplo de uso (os vetores de entrada precisam estar previamente ordenados)
v1 = [1, 4, 7, 10]
v2 = [2, 3, 6, 8, 12]

print("Vetor 1:", v1)
print("Vetor 2:", v2)
print("Resultado do Merge:", merge_vetores(v1, v2))
