'''
Exercício 9.12 Modifique o programa anterior para também registrar a linha e a
coluna de cada ocorrência da palavra no arquivo. Para isso, utilize listas nos valores
de cada palavra, guardando a linha e a coluna de cada ocorrência.

'''


import string
import sys


def mapear_posicoes_palavras(nome_arquivo):
    ocorrencias = {}

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            for num_linha, linha in enumerate(f, start=1):
                coluna = 1
                palavra_atual = []
                coluna_inicio = 1

                for char in linha:
                    # Se for letra, número ou underline, faz parte da palavra
                    if char not in string.punctuation and not char.isspace():
                        if not palavra_atual:
                            coluna_inicio = coluna
                        palavra_atual.append(char)
                    else:
                        # Encontrou separador: registra a palavra acumulada
                        if palavra_atual:
                            palavra = "".join(palavra_atual).lower()
                            if palavra not in ocorrencias:
                                ocorrencias[palavra] = []
                            ocorrencias[palavra].append(
                                (num_linha, coluna_inicio))
                            palavra_atual = []

                    coluna += 1

                # Trata palavra no final da linha (caso não termine com espaço/quebra)
                if palavra_atual:
                    palavra = "".join(palavra_atual).lower()
                    if palavra not in ocorrencias:
                        ocorrencias[palavra] = []
                    ocorrencias[palavra].append((num_linha, coluna_inicio))

        return ocorrencias

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        sys.exit(1)
    except PermissionError:
        print(f"Erro: Sem permissão para ler o arquivo '{nome_arquivo}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <nome_do_arquivo>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]
    resultado = mapear_posicoes_palavras(caminho_arquivo)

    print(
        f"\nDicionário de ocorrências ({len(resultado)} palavras distintas):\n")
    for palavra, posicoes in sorted(resultado.items()):
        total = len(posicoes)
        posicoes_str = ", ".join(f"(L:{l}, C:{c})" for l, c in posicoes)
        print(f"'{palavra}' ({total}x): [{posicoes_str}]")


if __name__ == "__main__":
    main()
