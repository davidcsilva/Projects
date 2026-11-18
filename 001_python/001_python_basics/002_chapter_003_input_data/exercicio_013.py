'''
Escreva um programa que converta uma temperatura digitada em
°C em °F. A fórmula para essa conversão é:
F=9×C/5 + 32
'''

temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = (9 * temperatura_celsius / 5) + 32

print("A temperatura em Fahrenheit é: ", temperatura_fahrenheit)
