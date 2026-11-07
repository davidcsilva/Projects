'''
Faça um programa que solicite o preço de uma mercadoria e o per-
centual de desconto. Exiba o valor do desconto e o preço a pagar.
'''

preco = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

desconto = preco * (percentual_desconto / 100)
preco_a_pagar = preco - desconto

print("O valor do desconto é: ", desconto)
print("O preço a pagar é: ", preco_a_pagar)
