'''
Exercício 9.8 Modifique o programa anterior para também receber o número de
caracteres por linha e o número de páginas por folha pela linha de comando.

'''

import sys


def quebrar_linha(linha, largura):
    """Quebra uma linha em pedaços de no máximo `largura` caracteres."""
    if not linha:
        return [""]
    return [linha[i: i + largura] for i in range(0, len(linha), largura)]


def paginar_arquivo(nome_entrada, largura_max, linhas_por_pagina, nome_saida="saida_paginada.txt"):
    try:
        linhas_processadas = []

        # 1. Lê e divide as linhas respeitando a largura informada
        with open(nome_entrada, "r", encoding="utf-8") as f_in:
            for linha in f_in:
                conteudo = linha.rstrip("\r\n")
                partes = quebrar_linha(conteudo, largura_max)
                linhas_processadas.extend(partes)

        # 2. Configura o espaço para conteúdo e reserva 1 linha para o rodapé
        linhas_uteis = linhas_por_pagina - 1
        total_linhas = len(linhas_processadas)
        pagina_atual = 1

        with open(nome_saida, "w", encoding="utf-8") as f_out:
            for inicio in range(0, total_linhas, linhas_uteis):
                bloco = linhas_processadas[inicio: inicio + linhas_uteis]

                # Escreve o texto da página
                for linha in bloco:
                    f_out.write(linha + "\n")

                # Preenche com linhas vazias até a penúltima linha se a página estiver incompleta
                linhas_faltantes = linhas_uteis - len(bloco)
                for _ in range(linhas_faltantes):
                    f_out.write("\n")

                # Última linha da página: rodapé formatado
                rodape = f"{nome_entrada} - Página {pagina_atual}"
                if len(rodape) > largura_max:
                    rodape = f"Pág {pagina_atual}"[:largura_max]
                f_out.write(rodape.rjust(largura_max) + "\n")

                pagina_atual += 1

        print(
            f"Arquivo paginado com sucesso em '{nome_saida}' "
            f"({pagina_atual - 1} página(s), {linhas_por_pagina} linhas/pág, {largura_max} cols)."
        )

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_entrada}' não foi encontrado.")
        sys.exit(1)
    except PermissionError:
        print(f"Erro: Sem permissão para ler ou escrever arquivos.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 4:
        print(
            f"Uso: python {sys.argv[0]} <arquivo> <caracteres_por_linha> <linhas_por_pagina> [arquivo_saida]")
        sys.exit(1)

    arquivo_origem = sys.argv[1]

    try:
        caracteres_por_linha = int(sys.argv[2])
        linhas_por_pagina = int(sys.argv[3])
    except ValueError:
        print("Erro: Os parâmetros <caracteres_por_linha> e <linhas_por_pagina> devem ser números inteiros.")
        sys.exit(1)

    if caracteres_por_linha < 10 or linhas_por_pagina < 2:
        print("Erro: Forneça ao menos 10 caracteres por linha e no mínimo 2 linhas por página (1 de texto + 1 rodapé).")
        sys.exit(1)

    arquivo_destino = sys.argv[4] if len(
        sys.argv) > 4 else "saida_paginada.txt"

    paginar_arquivo(arquivo_origem, caracteres_por_linha,
                    linhas_por_pagina, arquivo_destino)


if __name__ == "__main__":
    main()
