'''
Escreva um programa que leia duas strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posição de início.
1ª string: AABBEFAATT
2ª string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT
'''

string1 = input("1ª string: ")
string2 = input("2ª string: ")

posicao = string1.find(string2)

if posicao != -1:
    print(f"Resultado: {string2} encontrado na posição {posicao} de {string1}")
else:
    print(f"Resultado: {string2} não foi encontrado em {string1}")
