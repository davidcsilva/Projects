'''
O problema das OITO RAINHAS é um famoso problema relativo ao xadrez que tem por objetivo
situar oito rainhas em um tabuleiro de xadrez, de maneira que nenhuma delas seja capaz de
atacar qualquer outra. Uma rainha pode se movimentar em qualquer número de casas (quadrados)
verticalmente, horizontalmente ou nas diagonais no tabuleiro (um quadriculado de 8 por 8).
Escreva um programa que contenha uma rotina recursiva que resolva o problema das Oito Rainhas.

Sugestão da questão:
Proposta de numeração de casas do tabuleiro:
- i (número fila / linha): 1 a 8
- j (número coluna): 1 a 8
- fila i: i = constante
- diagonal ascendente: (i + j) = constante
- diagonal descendente: (i - j) = constante
'''


def resolver_oito_rainhas(n: int = 8) -> list[list[int]]:
    """Resolve o problema das N Rainhas utilizando recursão com backtracking.

    Retorna:
        list[list[int]]: Lista contendo todas as soluções encontradas. Cada solução é
        uma lista de tamanho n onde o índice representa a linha (0 a n-1) e o valor
        representa a coluna (0 a n-1) onde a rainha foi posicionada.
    """
    solucoes: list[list[int]] = []
    tabuleiro: list[int] = [-1] * n  # tabuleiro[linha] = coluna

    # Conjuntos para checagem rápida em O(1)
    colunas_ocupadas: set[int] = set()
    diagonais_soma: set[int] = set()  # (i + j) = constante
    diagonais_subtracao: set[int] = set()  # (i - j) = constante

    def posicionar_rainha(linha: int):
        # Caso base: todas as rainhas (de 0 a n-1) foram posicionadas com sucesso
        if linha == n:
            solucoes.append(list(tabuleiro))
            return

        # Tenta posicionar uma rainha em cada coluna da linha atual
        for coluna in range(n):
            diag_soma = linha + coluna
            diag_sub = linha - coluna

            # Verifica se a posição está sob ataque
            if (
                coluna in colunas_ocupadas
                or diag_soma in diagonais_soma
                or diag_sub in diagonais_subtracao
            ):
                continue

            # Passo: posiciona a rainha
            tabuleiro[linha] = coluna
            colunas_ocupadas.add(coluna)
            diagonais_soma.add(diag_soma)
            diagonais_subtracao.add(diag_sub)

            # Passo recursivo: avança para a próxima linha
            posicionar_rainha(linha + 1)

            # Backtracking: desfaz a jogada para testar outras possibilidades
            tabuleiro[linha] = -1
            colunas_ocupadas.remove(coluna)
            diagonais_soma.remove(diag_soma)
            diagonais_subtracao.remove(diag_sub)

    # Inicia a recursão a partir da primeira linha (linha 0)
    posicionar_rainha(0)
    return solucoes


def exibir_tabuleiro(solucao: list[int]) -> None:
    """Exibe o tabuleiro de xadrez formatado com as posições das rainhas (R)."""
    n = len(solucao)
    print("    " + " ".join(f"{j + 1}" for j in range(n)))
    print("  +" + "--" * n + "-+")

    for i in range(n):
        linha_str = []
        for j in range(n):
            if solucao[i] == j:
                linha_str.append("R")
            else:
                linha_str.append(".")
        print(f"{i + 1} | " + " ".join(linha_str) + " |")

    print("  +" + "--" * n + "-+")


if __name__ == "__main__":
    print("=== RESOLVENDO O PROBLEMA DAS OITO RAINHAS ===")
    solucoes = resolver_oito_rainhas(8)

    print(f"\nTotal de soluções possíveis encontradas: {len(solucoes)}")

    # Exibindo a primeira solução
    print("\nRepresentação gráfica da 1ª solução encontrada:")
    exibir_tabuleiro(solucoes[0])

    # Posições coordenadas (linha, coluna) de 1 a 8:
    posicoes_1_a_8 = [(i + 1, col + 1) for i, col in enumerate(solucoes[0])]
    print(f"\nCoordenadas (linha, coluna): {posicoes_1_a_8}")
