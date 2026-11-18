'''
Exercício 9.36 Utilizando a função os.walk, crie um programa que calcule o es-
paço ocupado por cada diretório e subdiretório, gerando uma página html com
os resultados.


'''


# Exercício 9.36: Calcula o espaço ocupado por cada diretório e subdiretório e gera página HTML

import os
import sys


def formatar_tamanho(bytes_total):
    """Retorna o tamanho formatado em B, KB, MB, GB ou TB."""
    for unidade in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_total < 1024.0:
            return f"{bytes_total:.1f} {unidade}"
        bytes_total /= 1024.0
    return f"{bytes_total:.1f} PB"


def calcular_espaco_diretorios(diretorio_raiz):
    """
    Percorre a árvore de diretórios utilizando os.walk.
    Calcula:
      - espaco_proprio: bytes dos arquivos contidos diretamente naquela pasta.
      - espaco_total: bytes acumulados somando a pasta e todas as suas subpastas.
    """
    espaco_proprio = {}

    # 1. Calcula o tamanho direto dos arquivos de cada pasta
    for raiz, _, arquivos in os.walk(diretorio_raiz):
        tamanho_pasta = 0
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            try:
                tamanho_pasta += os.path.getsize(caminho_completo)
            except OSError:
                continue
        espaco_proprio[raiz] = tamanho_pasta

    # 2. Acumula os tamanhos considerando os subdiretórios
    espaco_total = {}
    for pasta in espaco_proprio:
        total = 0
        pasta_padronizada = os.path.abspath(pasta)
        for outra_pasta, tamanho in espaco_proprio.items():
            outra_padronizada = os.path.abspath(outra_pasta)
            if outra_padronizada == pasta_padronizada or outra_padronizada.startswith(pasta_padronizada + os.sep):
                total += tamanho
        espaco_total[pasta] = total

    return espaco_proprio, espaco_total


def gerar_relatorio_html(diretorio_raiz, arquivo_saida="espaco_diretorios.html"):
    if not os.path.exists(diretorio_raiz):
        print(f"Erro: O caminho '{diretorio_raiz}' não existe.")
        sys.exit(1)

    if not os.path.isdir(diretorio_raiz):
        print(f"Erro: '{diretorio_raiz}' não é um diretório.")
        sys.exit(1)

    espaco_proprio, espaco_total = calcular_espaco_diretorios(diretorio_raiz)
    diretorios_ordenados = sorted(espaco_proprio.keys())

    with open(arquivo_saida, "w", encoding="utf-8") as html:
        html.write("<!DOCTYPE html>\n")
        html.write('<html lang="pt-BR">\n')
        html.write("<head>\n")
        html.write('  <meta charset="utf-8">\n')
        html.write("  <title>Espaço Ocupado por Diretórios</title>\n")
        html.write("  <style>\n")
        html.write(
            "    body { font-family: sans-serif; margin: 24px; color: #333; }\n")
        html.write("    h1 { color: #2c3e50; font-size: 22px; }\n")
        html.write(
            "    table { border-collapse: collapse; width: 100%; margin-top: 16px; }\n")
        html.write(
            "    th, td { border: 1px solid #ddd; padding: 10px 14px; text-align: left; }\n")
        html.write("    th { background-color: #f4f6f7; font-weight: 600; }\n")
        html.write("    tr:nth-child(even) { background-color: #fafbfc; }\n")
        html.write("    tr:hover { background-color: #f1f4f6; }\n")
        html.write("    .tamanho { text-align: right; width: 180px; }\n")
        html.write("  </style>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write(
            f"  <h1>Espaço Ocupado por Diretório: {os.path.abspath(diretorio_raiz)}</h1>\n")
        html.write("  <table>\n")
        html.write("    <thead>\n")
        html.write("      <tr>\n")
        html.write("        <th>Diretório</th>\n")
        html.write("        <th class='tamanho'>Espaço Próprio (Direto)</th>\n")
        html.write(
            "        <th class='tamanho'>Espaço Total (com Subpastas)</th>\n")
        html.write("      </tr>\n")
        html.write("    </thead>\n")
        html.write("    <tbody>\n")

        for d in diretorios_ordenados:
            caminho_relativo = os.path.relpath(d, diretorio_raiz)
            if caminho_relativo == ".":
                caminho_relativo = f"{os.path.basename(os.path.abspath(diretorio_raiz))} (raiz)"

            bytes_diretos = espaco_proprio[d]
            bytes_acumulados = espaco_total[d]

            html.write("      <tr>\n")
            html.write(f"        <td>{caminho_relativo}</td>\n")
            html.write(
                f"        <td class='tamanho'>{formatar_tamanho(bytes_diretos)} ({bytes_diretos} B)</td>\n")
            html.write(
                f"        <td class='tamanho'><strong>{formatar_tamanho(bytes_acumulados)}</strong> ({bytes_acumulados} B)</td>\n")
            html.write("      </tr>\n")

        html.write("    </tbody>\n")
        html.write("  </table>\n")
        total_raiz = espaco_total.get(diretorio_raiz, 0)
        html.write(
            f"  <p style='margin-top: 18px;'><strong>Total de diretórios:</strong> {len(diretorios_ordenados)} | <strong>Ocupação total da raiz:</strong> {formatar_tamanho(total_raiz)}</p>\n")
        html.write("</body>\n")
        html.write("</html>\n")

    print(
        f"Relatório gerado em '{arquivo_saida}' com {len(diretorios_ordenados)} diretório(s).")


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <diretorio>")
        sys.exit(1)

    caminho = sys.argv[1]
    gerar_relatorio_html(caminho)


if __name__ == "__main__":
    main()
