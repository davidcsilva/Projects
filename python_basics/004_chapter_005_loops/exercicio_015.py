'''
Escreva um programa para controlar uma pequena máquina registra-
dora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
CódigoPreço
10,50
21,00
34,00
57,00
98,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”.
'''

total_compras = 0.0

while True:
    codigo = int(input("Digite o código do produto (0 para finalizar): "))

    # Condição de saída
    if codigo == 0:
        break

    # Validação do código e atribuição do preço
    preco = 0.0
    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido")
        continue  # Volta para o início do loop sem pedir a quantidade

    # Leitura da quantidade e acúmulo do valor total
    quantidade = int(input("Digite a quantidade comprada: "))
    total_compras += preco * quantidade

print(f"\nTotal das compras: R$ {total_compras:.2f}")
