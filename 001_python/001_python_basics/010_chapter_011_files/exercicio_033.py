'''
Exercício 9.33 Crie um programa que gere uma página html com links para todos
os arquivos jpg e png encontrados a partir de um diretório informado na linha
de comando.


'''


import os
import sys

EXTENSOES_VALIDAS = (".jpg", ".jpeg", ".png")


def gerar_pagina_imagens(diretorio_raiz, arquivo_saida="imagens.html"):
    if not os.path.exists(diretorio_raiz):
        print(f"Erro: O diretório '{diretorio_raiz}' não existe.")
        sys.exit(1)

    if not os.path.isdir(diretorio_raiz):
        print(f"Erro: '{diretorio_raiz}' não é um diretório.")
        sys.exit(1)

    imagens_encontradas = []

    # os.walk percorre o diretório e todas as subpastas recursivamente
    for raiz, _, arquivos in os.walk(diretorio_raiz):
        for arquivo in arquivos:
            # Verifica se a extensão do arquivo é de imagem suportada
            if arquivo.lower().endswith(EXTENSOES_VALIDAS):
                caminho_completo = os.path.join(raiz, arquivo)
                imagens_encontradas.append(caminho_completo)

    # Criação do arquivo HTML
    with open(arquivo_saida, "w", encoding="utf-8") as html:
        html.write("<!DOCTYPE html>\n")
        html.write('<html lang="pt-BR">\n')
        html.write("<head>\n")
        html.write('  <meta charset="utf-8">\n')
        html.write("  <title>Galeria de Imagens</title>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write(f"  <h1>Imagens encontradas em: {diretorio_raiz}</h1>\n")

        if not imagens_encontradas:
            html.write("  <p>Nenhuma imagem JPG ou PNG foi encontrada.</p>\n")
        else:
            html.write(
                f"  <p>Total de imagens: {len(imagens_encontradas)}</p>\n")
            html.write("  <ul>\n")
            for caminho_img in sorted(imagens_encontradas):
                # os.path.basename obtém apenas o nome do arquivo para exibir no texto do link
                nome_arquivo = os.path.basename(caminho_img)
                html.write(
                    f'    <li><a href="{caminho_img}" target="_blank">{nome_arquivo}</a> ({caminho_img})</li>\n')
            html.write("  </ul>\n")

        html.write("</body>\n")
        html.write("</html>\n")

    print(
        f"Página gerada com sucesso: '{arquivo_saida}' com {len(imagens_encontradas)} imagem(ns).")


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <diretorio>")
        sys.exit(1)

    diretorio = sys.argv[1]
    gerar_pagina_imagens(diretorio)


if __name__ == "__main__":
    main()
