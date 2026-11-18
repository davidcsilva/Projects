'''
Exercício 9.14 Crie um programa que leia um arquivo-texto e elimine os espaços
repetidos entre as palavras e no fim das linhas. O arquivo de saída também não
deve ter mais de uma linha em branco repetida.

'''


import sys


def limpar_texto(nome_origem, nome_destino="saida_limpa.txt"):
    try:
        linha_em_branco_anterior = False

        with open(nome_origem, "r", encoding="utf-8") as f_in, \
                open(nome_destino, "w", encoding="utf-8") as f_out:

            for linha in f_in:
                # Quebra por qualquer sequência de espaços em branco (espaços, tabs)
                palavras = linha.split()

                if not palavras:
                    # Linha em branco ou composta apenas de espaços
                    if not linha_em_branco_anterior:
                        f_out.write("\n")
                        linha_em_branco_anterior = True
                else:
                    # Junta as palavras com um único espaço entre elas
                    linha_formatada = " ".join(palavras)
                    f_out.write(linha_formatada + "\n")
                    linha_em_branco_anterior = False

        print(f"Arquivo limpo com sucesso! Salvo em '{nome_destino}'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_origem}' não foi encontrado.")
        sys.exit(1)
    except PermissionError:
        print("Erro: Sem permissão para ler ou escrever arquivos.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <arquivo_origem> [arquivo_destino]")
        sys.exit(1)

    arquivo_origem = sys.argv[1]
    arquivo_destino = sys.argv[2] if len(sys.argv) > 2 else "saida_limpa.txt"

    limpar_texto(arquivo_origem, arquivo_destino)


if __name__ == "__main__":
    main()
