'''
Exercício 9.9 Crie um programa que receba uma lista de nomes de arquivo e os
imprima, um por um.

'''

import sys


def imprimir_arquivo(nome_arquivo):
    print("=" * 60)
    print(f"Arquivo: {nome_arquivo}")
    print("=" * 60)

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(linha, end="")
        print("\n")  # Linha em branco ao final do arquivo para separar

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.\n")
    except PermissionError:
        print(f"Erro: Sem permissão para ler '{nome_arquivo}'.\n")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler '{nome_arquivo}': {e}\n")


def main():
    # sys.argv[0] é o nome do próprio script
    # sys.argv[1:] contém a lista com todos os arquivos passados
    arquivos = sys.argv[1:]

    if not arquivos:
        print(
            f"Uso: python {sys.argv[0]} <arquivo1> [arquivo2] [arquivo3] ...")
        sys.exit(1)

    for arquivo in arquivos:
        imprimir_arquivo(arquivo)


if __name__ == "__main__":
    main()
