'''
Exercício 9.4 Crie um programa que receba o nome de dois arquivos como pa-
râmetros da linha de comando e que gere um arquivo de saída com as linhas do
primeiro e do segundo arquivo.

'''


import sys


def main():
    # Verifica se foram fornecidos os nomes dos dois arquivos de entrada
    if len(sys.argv) < 3:
        print(f"Uso: python {sys.argv[0]} <arquivo1> <arquivo2>")
        sys.exit(1)

    arquivo1 = sys.argv[1]
    arquivo2 = sys.argv[2]
    arquivo_saida = "saida.txt"

    try:
        with open(arquivo_saida, "w", encoding="utf-8") as f_out:
            # Copia todas as linhas do primeiro arquivo
            with open(arquivo1, "r", encoding="utf-8") as f1:
                for linha in f1:
                    f_out.write(linha)

            # Copia todas as linhas do segundo arquivo
            with open(arquivo2, "r", encoding="utf-8") as f2:
                for linha in f2:
                    f_out.write(linha)

        print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

    except FileNotFoundError as e:
        print(f"Erro: O arquivo '{e.filename}' não foi encontrado.")
        sys.exit(1)
    except PermissionError as e:
        print(f"Erro de permissão: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
