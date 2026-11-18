'''
binary search
'''


def busca_binaria(lista, alvo):
    # Inicializa os ponteiros de início e fim da lista
    inicio = 0
    fim = len(lista) - 1

    # Continua enquanto o ponteiro de início não ultrapassar o de fim
    while inicio <= fim:
        # Calcula o índice do meio
        meio = (inicio + fim) // 2

        # Se o elemento do meio for o alvo, retorna o índice
        if lista[meio] == alvo:
            return meio
        # Se o alvo for maior, ignora a metade esquerda
        elif lista[meio] < alvo:
            inicio = meio + 1
        # Se o alvo for menor, ignora a metade direita
        else:
            fim = meio - 1

    # Se o loop terminar sem encontrar, retorna -1
    return -1


# Exemplo de uso (a lista DEVE estar ordenada)
numeros_ordenados = [2, 4, 8, 15, 16, 23, 42]
procurado = 23

resultado = busca_binaria(numeros_ordenados, procurado)

if resultado != -1:
    print(f"Elemento {procurado} encontrado no índice {resultado}.")
else:
    print(f"Elemento {procurado} não encontrado na lista.")
