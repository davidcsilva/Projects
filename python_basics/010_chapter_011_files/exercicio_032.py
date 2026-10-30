'''
Exercício 9.32 Modifique o programa da listagem 9.20 de forma a receber o nome
do arquivo ou diretório a verificar pela linha de comando. Imprima se existir e se
for um arquivo ou um diretório.


'''


import os
import sys

# Verifica se o parâmetro foi passado pela linha de comando
if len(sys.argv) < 2:
    print(f"Uso: python {sys.argv[0]} <caminho_arquivo_ou_diretorio>")
    sys.exit(1)

caminho = sys.argv[1]

# Verifica se o caminho existe
if os.path.exists(caminho):
    if os.path.isdir(caminho):
        print(f"'{caminho}' existe e é um diretório.")
    elif os.path.isfile(caminho):
        print(f"'{caminho}' existe e é um arquivo.")
    else:
        print(
            f"'{caminho}' existe, mas é um tipo especial de item (ex: link simbólico, socket, etc.).")
else:
    print(f"'{caminho}' não existe.")
