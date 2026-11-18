'''
Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário.
'''

salario = float(input("Digite o valor do salário: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print("O valor do aumento é: ", aumento)
print("O novo salário é: ", novo_salario)
