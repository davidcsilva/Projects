'''
Escreva um programa que leia três strings. Imprima o resultado da
substituição na primeira, dos caracteres da segunda pelos da terceira.
1ª string: AATTCGAA
2ª string: TG
3ª string: AC
Resultado: AAAACCAA
'''

s1 = input("1ª string: ")
s2 = input("2ª string: ")
s3 = input("3ª string: ")

if len(s2) != len(s3):
    print("Erro: A 2ª e a 3ª string devem ter o mesmo tamanho para o mapeamento.")
else:
    # Cria a tabela de substituição de s2 para s3
    tabela = str.maketrans(s2, s3)
    resultado = s1.translate(tabela)
    print(f"Resultado: {resultado}")
