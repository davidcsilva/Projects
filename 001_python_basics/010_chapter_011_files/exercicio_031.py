'''
Exercício 9.31 Crie um programa que corrija o da listagem 9.20 de forma a verificar
se z existe e é um diretório.

'''
import os
import sys

# Recebe o nome/caminho do diretório (por linha de comando ou input)
if len(sys.argv) > 1:
    z = sys.argv[1]
else:
    z = input("Digite o caminho do diretório: ").strip()

# Verificações do Exercício 9.31:
if not os.path.exists(z):
    print(f"Erro: O caminho '{z}' não existe.")
elif not os.path.isdir(z):
    print(
        f"Erro: '{z}' existe, mas não é um diretório (é um arquivo ou outro tipo de item).")
else:
    print(f"\nConteúdo do diretório '{z}':")
    for item in os.listdir(z):
        print(f" - {item}")
