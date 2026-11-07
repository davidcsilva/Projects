'''
Exercício 9.10 Crie um programa que receba uma lista de nomes de arquivo e que
gere apenas um grande arquivo de saída.

'''

import sys


def concatenar_arquivos(lista_arquivos, arquivo_saida="arquivo_completo.txt"):
    total_processados = 0

    try:
        with open(arquivo_saida, "w", encoding="utf-8") as f_out:
            for nome_arquivo in lista_arquivos:
                try:
                    with open(nome_arquivo, "r", encoding="utf-8") as f_in:
                        for linha in f_in:
                            f_out.write(linha)

                        # Garante quebra de linha ao fim do arquivo para não colar no próximo
                        if not linha.endswith("\n"):
                            f_out.write("\n")

                    print(f"Adicionado: {nome_arquivo}")
                    total_processados += 1

                except FileNotFoundError:
                    print(
                        f"Aviso: Arquivo '{nome_arquivo}' não encontrado. Pulando...")
                except PermissionError:
                    print(
                        f"Aviso: Sem permissão para ler '{nome_arquivo}'. Pulando...")

        print("-" * 50)
        print(
            f"Concluído! {total_processados} arquivo(s) mesclado(s) em '{arquivo_saida}'.")

    except PermissionError:
        print(
            f"Erro: Sem permissão para escrever o arquivo '{arquivo_saida}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


def main():
    # sys.argv[1:] captura todos os arquivos informados após o nome do script
    arquivos = sys.argv[1:]

    if not arquivos:
        print(
            f"Uso: python {sys.argv[0]} <arquivo1> [arquivo2] [arquivo3] ...")
        sys.exit(1)

    concatenar_arquivos(arquivos)


if __name__ == "__main__":
    main()
