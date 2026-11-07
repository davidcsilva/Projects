'''
Exercício 9.35 Utilizando a função os.walk, crie uma página HTML com o nome
e tamanho de cada arquivo de um diretório passado e de seus subdiretórios.


'''


# Exercício 9.35: Gera página HTML com nome e tamanho dos arquivos de um diretório e subdiretórios

import os
import sys


def formatar_tamanho(bytes_total):
    """Retorna o tamanho formatado em B, KB, MB ou GB."""
    for unidade in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_total < 1024.0:
            return f"{bytes_total:.1f} {unidade}"
        bytes_total /= 1024.0
    return f"{bytes_total:.1f} PB"


def gerar_relatorio_diretorio(diretorio_raiz, arquivo_saida="arquivos.html"):
    if not os.path.exists(diretorio_raiz):
        print(f"Erro: O caminho '{diretorio_raiz}' não existe.")
        sys.exit(1)

    if not os.path.isdir(diretorio_raiz):
        print(f"Erro: '{diretorio_raiz}' não é um diretório.")
        sys.exit(1)

    with open(arquivo_saida, "w", encoding="utf-8") as html:
        html.write("<!DOCTYPE html>\n")
        html.write('<html lang="pt-BR">\n')
        html.write("<head>\n")
        html.write('  <meta charset="utf-8">\n')
        html.write("  <title>Lista de Arquivos e Tamanhos</title>\n")
        html.write("  <style>\n")
        html.write("    body { font-family: sans-serif; margin: 24px; }\n")
        html.write(
            "    table { border-collapse: collapse; width: 100%; margin-top: 16px; }\n")
        html.write(
            "    th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: left; }\n")
        html.write("    th { background-color: #f2f2f2; }\n")
        html.write("    tr:nth-child(even) { background-color: #fafafa; }\n")
        html.write("    .tamanho { text-align: right; width: 160px; }\n")
        html.write("  </style>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write(
            f"  <h1>Arquivos em: {os.path.abspath(diretorio_raiz)}</h1>\n")
        html.write("  <table>\n")
        html.write("    <thead>\n")
        html.write("      <tr>\n")
        html.write("        <th>Caminho / Nome do Arquivo</th>\n")
        html.write("        <th class='tamanho'>Tamanho</th>\n")
        html.write("      </tr>\n")
        html.write("    </thead>\n")
        html.write("    <tbody>\n")

        total_arquivos = 0
        total_bytes = 0

        # Percorre a pasta raiz e todas as subpastas
        for raiz, _, arquivos in os.walk(diretorio_raiz):
            for nome_arquivo in arquivos:
                caminho_completo = os.path.join(raiz, nome_arquivo)
                try:
                    tamanho = os.path.getsize(caminho_completo)
                    total_bytes += tamanho
                    total_arquivos += 1

                    # Caminho relativo para facilitar a leitura na tabela
                    caminho_relativo = os.path.relpath(
                        caminho_completo, diretorio_raiz)

                    html.write("      <tr>\n")
                    html.write(f"        <td>{caminho_relativo}</td>\n")
                    html.write(
                        f"        <td class='tamanho'>{formatar_tamanho(tamanho)} ({tamanho} B)</td>\n")
                    html.write("      </tr>\n")
                except OSError:
                    # Ignora arquivos temporários ou sem permissão de leitura
                    continue

        html.write("    </tbody>\n")
        html.write("  </table>\n")
        html.write(
            f"  <p><strong>Total de arquivos:</strong> {total_arquivos} | <strong>Tamanho total:</strong> {formatar_tamanho(total_bytes)}</p>\n")
        html.write("</body>\n")
        html.write("</html>\n")

    print(
        f"Página gerada com sucesso em '{arquivo_saida}' com {total_arquivos} arquivo(s).")


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <diretorio>")
        sys.exit(1)

    caminho = sys.argv[1]
    gerar_relatorio_diretorio(caminho)


if __name__ == "__main__":
    main()
