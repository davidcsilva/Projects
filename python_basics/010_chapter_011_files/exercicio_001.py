'''
Escreva um programa que receba o nome de um arquivo pela linha
de comando e que imprima todas as linhas desse arquivo.

'''

import sys


def main():
    # Verifica se o nome do arquivo foi fornecido nos argumentos
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <nome_do_arquivo>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                # O parâmetro end="" evita imprimir quebras de linha duplas,
                # já que cada linha lida já contém o caractere de nova linha (\n).
                print(linha, end="")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)
    except PermissionError:
        print(f"Erro: Sem permissão para ler o arquivo '{caminho_arquivo}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
