'''
Analise o programa da listagem 4.2. Responda o que acontece se o
primeiro e o segundo valores forem iguais? Explique.
'''
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:
    print("O primeiro valor é maior!")

else:
    print("O segundo valor é maior!")

# Se os valores forem iguais, o programa executará o bloco else, imprimindo "O segundo valor é maior!", porque a condição a > b será avaliada como falsa.
