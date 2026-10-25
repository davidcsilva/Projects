'''
Escreva um jogo da velha para dois jogadores. O jogo deve perguntar
onde você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
posição está livre. Verifique também quando um jogador venceu a partida. Um
jogo da velha pode ser visto como uma lista de 3 elementos, onde cada elemento
é outra lista, também com três elementos.
Exemplo do jogo:
X | O |
---+---+---
| X | X
---+---+---
|
| O
Onde cada posição pode ser vista como um número. Confira abaixo um exemplo
das posições mapeadas para a mesma posição de seu teclado numérico.
7 | 8 | 9
---+---+---
4 | 5 | 6
---+---+---
1 | 2 | 3
'''

# Inicialização do tabuleiro 3x3 com espaços em branco
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Dicionário mapeando as teclas numéricas (1-9) para as coordenadas [linha][coluna]
posicoes = {
    7: (0, 0), 8: (0, 1), 9: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    1: (2, 0), 2: (2, 1), 3: (2, 2)
}


def imprimir_tabuleiro(t):
    print(f" {t[0][0]} | {t[0][1]} | {t[0][2]} ")
    print("---+---+---")
    print(f" {t[1][0]} | {t[1][1]} | {t[1][2]} ")
    print("---+---+---")
    print(f" {t[2][0]} | {t[2][1]} | {t[2][2]} ")


def verificar_vitoria(t, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if t[i][0] == t[i][1] == t[i][2] == jogador:
            return True
        if t[0][i] == t[1][i] == t[2][i] == jogador:
            return True

    # Verifica diagonais
    if t[0][0] == t[1][1] == t[2][2] == jogador:
        return True
    if t[0][2] == t[1][1] == t[2][0] == jogador:
        return True

    return False


jogador_atual = "X"
jogadas = 0

print("=== JOGO DA VELHA ===")
print("Use o teclado numérico (1-9) para escolher a posição:\n")
print(" 7 | 8 | 9 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 1 | 2 | 3 \n")

while True:
    imprimir_tabuleiro(tabuleiro)

    try:
        escolha = int(
            input(f"\nJogador [{jogador_atual}], escolha uma posição (1-9): "))
    except ValueError:
        print("Entrada inválida! Digite um número entre 1 e 9.")
        continue

    if escolha not in posicoes:
        print("Posição inválida! Escolha um número de 1 a 9.")
        continue

    linha, coluna = posicoes[escolha]

    # Verificação se a posição está livre
    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada! Escolha outra.")
        continue

    # Realiza a jogada
    tabuleiro[linha][coluna] = jogador_atual
    jogadas += 1

    # Verificação de vitória
    if verificar_vitoria(tabuleiro, jogador_atual):
        imprimir_tabuleiro(tabuleiro)
        print(f"\nParabéns! O jogador [{jogador_atual}] venceu a partida!")
        break

    # Verificação de empate (deu velha)
    if jogadas == 9:
        imprimir_tabuleiro(tabuleiro)
        print("\nO jogo terminou em empate (Deu Velha)! ")
        break

    # Alterna o jogador entre 'X' e 'O'
    jogador_atual = "O" if jogador_atual == "X" else "X"
