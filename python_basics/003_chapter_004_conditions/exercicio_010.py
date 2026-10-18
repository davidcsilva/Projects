'''
Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta-
lação: R para residências, I para indústrias e C para comércios. Calcule o preço a
pagar de acordo com a tabela a seguir.
'''

print("Digite o tipo de instalação:")
print("R - Residência")
print("I - Indústria")
print("C - Comércio")

instalacao = input("Digite o tipo de instalação: ")

print("Digite a quantidade de kWh consumida: ")
kwh = float(input("Digite a quantidade de kWh consumida: "))

if instalacao == "R":
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65
elif instalacao == "I":
    if kwh <= 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
elif instalacao == "C":
    if kwh <= 1500:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
else:
    preco = 0

print("O preço a pagar é: R$ ", preco)
