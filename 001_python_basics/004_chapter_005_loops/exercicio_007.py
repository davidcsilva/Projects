'''
Modifique o programa anterior de forma que o usuário também
digite o início e o fim da tabuada, em vez de começar com 1 e 10.
'''

inicio = int(input("Digite o início da tabuada:"))
fim = int(input("Digite o fim da tabuada:"))

# Leitura dos dados do utilizador
numero = int(input("Qual a tabuada que deseja consultar? "))
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))

print(f"\nTabuada do {numero} (de {inicio} até {fim}):")

# O range precisa de + 1 no fim para incluir o número final
for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
