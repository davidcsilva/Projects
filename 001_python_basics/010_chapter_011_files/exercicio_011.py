'''
Exercício 9.11 Crie um programa que leia um arquivo e crie um dicionário onde
cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.

'''

import string
import sys


def contar_palavras(nome_arquivo):
    ocorrencias = {}

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                # Converte para minúsculas para padronizar
                linha_formatada = linha.lower()

                # Remove pontuações (vírgulas, pontos, exclamações, etc.)
                for pontuacao in string.punctuation:
                    linha_formatada = linha_formatada.replace(pontuacao, " ")

                # Quebra a linha nos espaços em branco
                palavras = linha_formatada.split()

                # Contabiliza no dicionário
                for palavra in palavras:
                    ocorrencias[palavra] = ocorrencias.get(palavra, 0) + 1

        return ocorrencias

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        sys.exit(1)
    except PermissionError:
        print(f"Erro: Sem permissão para ler o arquivo '{nome_arquivo}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <nome_do_arquivo>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]
    resultado = contar_palavras(caminho_arquivo)

    # Exibe as palavras e suas respectivas contagens
    print(
        f"\nDicionário de ocorrências ({len(resultado)} palavras distintas):\n")
    for palavra, total in sorted(resultado.items()):
        print(f"{palavra}: {total}")


if __name__ == "__main__":
    main()
