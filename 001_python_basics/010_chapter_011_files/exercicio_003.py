'''
Exercício 9.3 Crie um programa que leia os arquivos pares.txt e ímpares.txt e que
crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos,
de forma a preservar a ordem numérica.

'''


def mesclar_pares_e_impares():
    try:
        with open("pares.txt", "r", encoding="utf-8") as f_pares, \
                open("ímpares.txt", "r", encoding="utf-8") as f_impares, \
                open("pareseimpares.txt", "w", encoding="utf-8") as f_saida:

            linha_par = f_pares.readline()
            linha_impar = f_impares.readline()

            # Enquanto houver linhas para ler em ambos os arquivos
            while linha_par != "" and linha_impar != "":
                n_par = int(linha_par.strip())
                n_impar = int(linha_impar.strip())

                if n_par < n_impar:
                    f_saida.write(f"{n_par}\n")
                    linha_par = f_pares.readline()
                else:
                    f_saida.write(f"{n_impar}\n")
                    linha_impar = f_impares.readline()

            # Escreve os números restantes em pares.txt (se sobrarem)
            while linha_par != "":
                f_saida.write(f"{int(linha_par.strip())}\n")
                linha_par = f_pares.readline()

            # Escreve os números restantes em ímpares.txt (se sobrarem)
            while linha_impar != "":
                f_saida.write(f"{int(linha_impar.strip())}\n")
                linha_impar = f_impares.readline()

        print("Arquivo 'pareseimpares.txt' gerado com sucesso!")

    except FileNotFoundError as e:
        print(f"Erro ao abrir arquivo: {e.filename} não foi encontrado.")
    except ValueError:
        print("Erro: Um dos arquivos contém valores que não são números inteiros válidos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    mesclar_pares_e_impares()
