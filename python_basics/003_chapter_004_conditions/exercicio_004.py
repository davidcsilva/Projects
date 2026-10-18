'''
Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
10%. Para os inferiores ou iguais, de 15%.
'''

salario = float(input("Digite o salário do funcionário: R$ "))

if salario > 1250:
    aumento = salario * 0.10
    print("O aumento é de 10%!")
    print("O valor do aumento é de R$ {:.2f}".format(aumento))
    print("O novo salário é de R$ {:.2f}".format(salario + aumento))
else:
    aumento = salario * 0.15
    print("O aumento é de 15%!")
    print("O valor do aumento é de R$ {:.2f}".format(aumento))
    print("O novo salário é de R$ {:.2f}".format(salario + aumento))
