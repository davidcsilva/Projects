'''
screva um programa que leia um número e verifique se é ou não
um número primo. Para fazer essa verificação, calcule o resto da divisão do número
por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma
dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são
primos e que 2 é o único número primo que é par.
'''

# Leitura do número inteiro
numero = int(input("Digite um número inteiro: "))

# Trata casos especiais: números menores ou iguais a 1 não são primos
if numero <= 1:
    e_primo = False
# 2 é o único número primo par
elif numero == 2:
    e_primo = True
# Números pares maiores que 2 não são primos
elif numero % 2 == 0:
    e_primo = False
else:
    e_primo = True
    # Testar divisões por números ímpares de 3 até o número - 1
    divisor = 3
    while divisor < numero:
        if numero % divisor == 0:
            e_primo = False
            break  # Encontrou um divisor, não é necessário continuar
        divisor += 2

# Exibição do resultado
if e_primo:
    print(f"O número {numero} É PRIMO.")
else:
    print(f"O número {numero} NÃO É PRIMO.")
