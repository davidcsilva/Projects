'''
Exercício 9.15 Altere o programa da listagem 7.5, o jogo da forca. Utilize um arqui-
vo em que uma palavra seja gravada a cada linha. Use um editor de textos para
gerar o arquivo. Ao iniciar o programa, utilize esse arquivo para carregar a lista de
palavras. Experimente também perguntar o nome do jogador e gerar um arquivo
com o número de acertos dos cinco melhores.

'''

import random
import sys

ARQUIVO_PALAVRAS = "palavras.txt"
ARQUIVO_RANKING = "ranking.txt"


def carregar_palavras(caminho):
    """Carrega as palavras do arquivo ignorando linhas vazias."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            palavras = [linha.strip().lower() for linha in f if linha.strip()]
        if not palavras:
            print(f"Erro: O arquivo '{caminho}' está vazio.")
            sys.exit(1)
        return palavras
    except FileNotFoundError:
        print(
            f"Erro: Arquivo '{caminho}' não encontrado. Crie o arquivo com uma palavra por linha.")
        sys.exit(1)


def carregar_ranking(caminho):
    """Lê os recordes salvos no formato: Nome;Pontos."""
    ranking = []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if ";" in linha:
                    nome, pontos_str = linha.split(";", 1)
                    ranking.append((nome, int(pontos_str)))
    except FileNotFoundError:
        pass  # Arquivo ainda não existe na primeira execução
    return ranking


def salvar_ranking(caminho, ranking):
    """Salva os 5 melhores registros no arquivo."""
    with open(caminho, "w", encoding="utf-8") as f:
        for nome, pontos in ranking[:5]:
            f.write(f"{nome};{pontos}\n")


def exibir_ranking(ranking):
    """Exibe a tabela dos top 5 jogadores."""
    print("\n" + "=" * 30)
    print("      TOP 5 - RANKING")
    print("=" * 30)
    if not ranking:
        print("Nenhum recorde registrado ainda.")
    else:
        for posicao, (nome, pontos) in enumerate(ranking[:5], start=1):
            print(f"{posicao}º {nome:<15} - {pontos} acerto(s)")
    print("=" * 30 + "\n")


def jogar():
    print("--- JOGO DA FORCA ---")
    nome_jogador = input("Digite o seu nome: ").strip() or "Jogador"

    palavras = carregar_palavras(ARQUIVO_PALAVRAS)
    palavra_secreta = random.choice(palavras)

    digitadas = []
    acertos = []
    erros = 0

    while True:
        # Monta a visualização da palavra com os acertos
        senha = ""
        for letra in palavra_secreta:
            senha += letra if letra in acertos else "."
        print(f"\nPalavra: {senha}")

        # Condição de vitória
        if senha == palavra_secreta:
            print(f"\nParabéns, {nome_jogador}! Você venceu!")
            break

        tentativa = input("Digite uma letra: ").lower().strip()
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Digite apenas uma única letra válida.")
            continue

        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue

        digitadas.append(tentativa)

        if tentativa in palavra_secreta:
            acertos.append(tentativa)
        else:
            erros += 1
            print("Você errou!")
            # Desenho simples da forca
            print("X==:==")
            print("X  :  ")
            if erros >= 1:
                print("X  O  ")
            else:
                print("X")
            if erros == 2:
                print("X  |  ")
            elif erros == 3:
                print("X \\|  ")
            elif erros >= 4:
                print("X \\|/ ")
            else:
                print("X")
            if erros == 5:
                print("X /   ")
            elif erros >= 6:
                print("X / \\ ")
            else:
                print("X")
            print("X\n=======")

            if erros == 6:
                print(
                    f"\nEnforcado! A palavra secreta era: '{palavra_secreta}'")
                break

    # Pontuação: número de letras distintas que o jogador acertou
    total_acertos = len(acertos)
    print(f"\n{nome_jogador}, você acertou {total_acertos} letra(s).")

    # Atualiza e salva o ranking dos top 5
    ranking = carregar_ranking(ARQUIVO_RANKING)
    ranking.append((nome_jogador, total_acertos))
    # Ordena decrescente pela pontuação (acertos)
    ranking.sort(key=lambda item: item[1], reverse=True)

    salvar_ranking(ARQUIVO_RANKING, ranking)
    exibir_ranking(ranking)


if __name__ == "__main__":
    jogar()
