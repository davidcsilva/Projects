'''
Escreva um programa que leia duas strings e gere uma terceira apenas
com os caracteres que aparecem em uma delas.
1ª string: CTA
2ª string: ABC
3ª string: BT
A ordem dos caracteres da terceira string não é importante.
'''
s1 = input("1ª string: ")
s2 = input("2ª string: ")

# Calcula a diferença simétrica entre os caracteres
exclusivos = set(s1) ^ set(s2)

resultado = "".join(exclusivos)

print(f"3ª string: {resultado}")
