'''
Exercício 9.7 Crie um programa que leia um arquivo-texto e gere um arquivo de
saída paginado. Cada linha não deve conter mais de 76 caracteres. Cada página
terá no máximo 60 linhas. Adicione na última linha de cada página o número da
página atual e o nome do arquivo original.


'''


import sys

LARGURA_MAXIMA = 76
LINHAS_POR_PAGINA = 60  # 59 linhas de texto + 1 linha de rodapé


def quebrar_linha(linha, largura):
    """Quebra uma linha em pedaços de no máximo `largura` caracteres."""
    if not linha:
        return [""]
    return [linha[i: i + largura] for i in range(0, len(linha), largura)]


def paginar_arquivo(nome_entrada, nome_saida="saida_paginada.txt"):
    try:
        linhas_processadas = []

        # 1. Lê o arquivo e garante que nenhuma linha ultrapasse 76 caracteres
        with open(nome_entrada, "r", encoding="utf-8") as f_in:
            for linha in f_in:
                conteudo = linha.rstrip("\r\n")
                partes = quebrar_linha(conteudo, LARGURA_MAXIMA)
                linhas_processadas.extend(partes)

        # 2. Divide em páginas e adiciona o rodapé na linha 60
        linhas_uteis = LINHAS_POR_PAGINA - 1  # 59 linhas para texto
        total_linhas = len(linhas_processadas)
        pagina_atual = 1

        with open(nome_saida, "w", encoding="utf-8") as f_out:
            for inicio in range(0, total_linhas, linhas_uteis):
                bloco = linhas_processadas[inicio: inicio + linhas_uteis]

                # Escreve o conteúdo da página
                for linha in bloco:
                    f_out.write(linha + "\n")

                # Preenche com linhas em branco se for a última página incompleta
                linhas_faltantes = linhas_uteis - len(bloco)
                for _ in range(linhas_faltantes):
                    f_out.write("\n")

                # Linha 60: Rodapé com nome do arquivo e número da página
                rodape = f"{nome_entrada} - Página {pagina_atual}"
                # Ajusta o rodapé centralizado ou alinhado à direita respeitando a largura
                f_out.write(rodape.rjust(LARGURA_MAXIMA) + "\n")

                pagina_atual += 1

        print(
            f"Arquivo paginado com sucesso em '{nome_saida}' ({pagina_atual - 1} página(s))."
        )

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_entrada}' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <nome_do_arquivo> [arquivo_saida]")
        sys.exit(1)

    arquivo_origem = sys.argv[1]
    arquivo_destino = sys.argv[2] if len(
        sys.argv) > 2 else "saida_paginada.txt"

    paginar_arquivo(arquivo_origem, arquivo_destino)


if __name__ == "__main__":
    main()
