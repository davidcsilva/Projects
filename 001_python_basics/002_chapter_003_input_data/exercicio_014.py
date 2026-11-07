'''
Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
dia e R$ 0,15 por km rodado.
'''
km_rodados = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(
    input("Digite a quantidade de dias pelos quais o carro foi alugado: "))

preco = (dias_alugados * 60) + (km_rodados * 0.15)

print("O preço a pagar é: R$", preco)
