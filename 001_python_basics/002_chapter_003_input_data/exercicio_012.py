
'''
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''

distancia = float(input("Digite a distância a percorrer (em km): "))
velocidade_media = float(
    input("Digite a velocidade média esperada (em km/h): "))

tempo = distancia / velocidade_media

print("O tempo estimado de viagem é de:", tempo, "horas")
