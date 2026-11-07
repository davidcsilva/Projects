'''
Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
'''
cigarros_por_dia = int(
    input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumados = int(input("Digite quantos anos você já fumou: "))

dias_de_vida = (cigarros_por_dia * 10) * anos_fumados * 365

print("Você perdeu", dias_de_vida, "dias de vida.")
