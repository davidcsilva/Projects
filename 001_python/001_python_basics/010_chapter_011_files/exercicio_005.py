'''

Exercício 9.5 Crie um programa que inverta a ordem das linhas do arquivo pares.
txt. A primeira linha deve conter o maior número; e a última, o menor.


'''


def inverter_pares():
    nome_arquivo_entrada = "pares.txt"
    nome_arquivo_saida = "pares_invertido.txt"

    try:
        # Lê todas as linhas do arquivo original
        with open(nome_arquivo_entrada, "r", encoding="utf-8") as f_entrada:
            linhas = f_entrada.readlines()

        # Inverte a ordem das linhas
        linhas_invertidas = reversed(linhas)

        # Grava as linhas na ordem invertida
        with open(nome_arquivo_saida, "w", encoding="utf-8") as f_saida:
            for linha in linhas_invertidas:
                # Garante que a linha termina com quebra de linha antes de salvar
                if not linha.endswith("\n"):
                    linha += "\n"
                f_saida.write(linha)

        print(
            f"Arquivo '{nome_arquivo_saida}' criado com as linhas invertidas com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    inverter_pares()
