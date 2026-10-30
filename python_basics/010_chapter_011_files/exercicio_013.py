'''
Exercício 9.13 Crie um programa que imprima as linhas de um arquivo. Esse pro-
grama deve receber três parâmetros pela linha de comando: o nome do arquivo,
a linha inicial e a última linha a imprimir.

'''

import sys


def imprimir_linhas(nome_arquivo, inicio, fim):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                # Se o número da linha estiver no intervalo desejado, imprime
                if inicio <= numero_linha <= fim:
                    print(linha, end="")
                # Se já ultrapassou a linha final, interrompe a leitura para economizar processamento
                elif numero_linha > fim:
                    break

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
    # sys.argv[0] é o script; os argumentos úteis começam em sys.argv[1]
    if len(sys.argv) < 4:
        print(
            f"Uso: python {sys.argv[0]} <nome_do_arquivo> <linha_inicial> <linha_final>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]

    # Converte e valida os valores das linhas
    try:
        linha_inicio = int(sys.argv[2])
        linha_fim = int(sys.argv[3])
    except ValueError:
        print("Erro: A linha inicial e a linha final devem ser números inteiros.")
        sys.exit(1)

    if linha_inicio < 1:
        print("Erro: A linha inicial deve ser maior ou igual a 1.")
        sys.exit(1)

    if linha_fim < linha_inicio:
        print("Erro: A linha final não pode ser menor que a linha inicial.")
        sys.exit(1)

    imprimir_linhas(caminho_arquivo, linha_inicio, linha_fim)


if __name__ == "__main__":
    main()
