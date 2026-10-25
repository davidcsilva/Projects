'''
Escreva um programa que leia duas strings e gere uma terceira, na
qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
3ª string: AAAA
'''

s1 = input("1ª string: ")
s2 = input("2ª string: ")

resultado_lista = []

for char in s1:
    if char not in s2:
        resultado_lista.append(char)

s3 = "".join(resultado_lista)

print(f"3ª string: {s3}")
