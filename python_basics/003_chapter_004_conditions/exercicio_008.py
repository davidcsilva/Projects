'''
Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
'''


num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Não é possível dividir por zero!")
    resultado = num1 / num2
else:
    resultado = "Operação inválida"

print(f"O resultado da operação é: {resultado}")
