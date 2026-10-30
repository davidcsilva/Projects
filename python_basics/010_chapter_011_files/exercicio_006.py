'''
Exercício 9.6 Modifique o programa da listagem 9.6 para imprimir 40 vezes o
símbolo de = se este for o primeiro caractere da linha. Adicione também a opção
para parar de imprimir até que se pressione a tecla Enter cada vez que uma linha
iniciar com . como primeiro caractere.

'''


import sys


def processa_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                # Remove apenas a quebra de linha do final
                linha_conteudo = linha.rstrip("\r\n")

                # Se a linha estiver vazia, apenas imprime a linha em branco
                if not linha_conteudo:
                    print()
                    continue

                primeiro_caractere = linha_conteudo[0]

                if primeiro_caractere == "=":
                    # Imprime 40 vezes o símbolo '='
                    print("=" * 40)
                elif primeiro_caractere == ".":
                    # Pausa a execução até o usuário pressionar Enter
                    input("Pressione Enter para continuar...")
                else:
                    # Imprime a linha normalmente
                    print(linha_conteudo)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <nome_do_arquivo>")
        sys.exit(1)

    processa_arquivo(sys.argv[1])


if __name__ == "__main__":
    main()
