'''
Escreva um programa que leia duas strings e gere uma terceira com
os caracteres comuns às duas strings lidas.
1ª string: AAACTBF
2ª string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas
as letras comuns a ambas.
'''
s1 = input("1ª string: ")
s2 = input("2ª string: ")

# Converte as strings em conjuntos e calcula a interseção (&)
comuns = set(s1) & set(s2)

# Junta os caracteres do conjunto em uma única string
resultado = "".join(comuns)

print(f"Resultado: {resultado}")
