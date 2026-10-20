'''
Modifique o exemplo para pesquisar dois valores. Em vez de apenas
p, leia outro valor v que também será procurado. Na impressão, indique qual dos
dois valores foi achado primeiro.
'''

L = [15, 7, 27, 39, 12, 80]

p = int(input("Digite o primeiro valor a procurar (p): "))
v = int(input("Digite o segundo valor a procurar (v): "))

x = 0
achou_p = -1  # Guardará a posição de p, se encontrado
achou_v = -1  # Guardará a posição de v, se encontrado

while x < len(L):
    if L[x] == p and achou_p == -1:
        achou_p = x
    if L[x] == v and achou_v == -1:
        achou_v = x

    # Se já encontrou ambos os elementos, pode interromper o loop antecipadamente
    if achou_p != -1 and achou_v != -1:
        break

    x += 1

# Verificação e exibição dos resultados
if achou_p != -1 and achou_v != -1:
    if achou_p < achou_v:
        print(f"O valor {p} foi achado primeiro (posição {achou_p}).")
        print(f"O valor {v} foi achado depois (posição {achou_v}).")
    elif achou_v < achou_p:
        print(f"O valor {v} foi achado primeiro (posição {achou_v}).")
        print(f"O valor {p} foi achado depois (posição {achou_p}).")
    else:
        # Ocorre apenas se p == v
        print(
            f"Os dois valores são iguais e foram encontrados na posição {achou_p}.")

elif achou_p != -1:
    print(f"Apenas o valor {p} foi achado na posição {achou_p}.")
    print(f"O valor {v} não foi encontrado.")

elif achou_v != -1:
    print(f"Apenas o valor {v} foi achado na posição {achou_v}.")
    print(f"O valor {p} não foi encontrado.")

else:
    print(f"Nenhum dos dois valores ({p} e {v}) foi encontrado na lista.")
