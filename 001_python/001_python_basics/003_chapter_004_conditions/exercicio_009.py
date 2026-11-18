'''
Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar.
'''

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite a quantidade de anos para pagar: "))

meses = anos * 12
prestacao = valor_casa / meses
limite_prestacao = salario * 0.30

if prestacao <= limite_prestacao:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo reprovado!")
