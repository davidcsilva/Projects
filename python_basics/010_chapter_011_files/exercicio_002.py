'''
Exercício 9.2 Modifique o programa do exercício 9.1 para que receba mais
dois parâmetros: a linha de início e a de fim para impressão. O programa
deve imprimir apenas as linhas entre esses dois valores (incluindo as linhas de
início e fim).

'''


import sys


def main():
    # Verifica se foram fornecidos os 3 parâmetros necessários
    if len(sys.argv) < 4:
        print(
            f"Uso: python {sys.argv[0]} <nome_do_arquivo> <linha_inicio> <linha_fim>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]

    # Converte os parâmetros de linha para inteiros
    try:
        linha_inicio = int(sys.argv[2])
        linha_fim = int(sys.argv[3])
    except ValueError:
        print(
            "Erro: Os parâmetros <linha_inicio> e <linha_fim> devem ser números inteiros.")
        sys.exit(1)

    if linha_inicio < 1 or linha_fim < linha_inicio:
        print("Erro: Intervalo inválido. Certifique-se de que linha_inicio >= 1 e linha_fim >= linha_inicio.")
        sys.exit(1)

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            # enumerate com start=1 para contar as linhas a partir de 1
            for numero_linha, conteudo_linha in enumerate(arquivo, start=1):
                if linha_inicio <= numero_linha <= linha_fim:
                    print(conteudo_linha, end="")
                elif numero_linha > linha_fim:
                    # Interrompe a leitura se já ultrapassou a linha de fim
                    break

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
