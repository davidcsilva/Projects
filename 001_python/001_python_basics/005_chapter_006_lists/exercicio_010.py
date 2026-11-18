'''
Modifique o programa do exercício 6.9 de forma a pesquisar p e v
em toda a lista e informando o usuário a posição onde p e a posição onde v foram
encontrados.
'''
L = [15, 7, 27, 39, 12, 7, 80, 27, 15]

p = int(input("Digite o primeiro valor a procurar (p): "))
v = int(input("Digite o segundo valor a procurar (v): "))

posicoes_p = []
posicoes_v = []

x = 0
while x < len(L):
    if L[x] == p:
        posicoes_p.append(x)
    if L[x] == v:
        posicoes_v.append(x)
    x += 1

print("\n--- RESULTADOS DA BUSCA ---")

# Exibição dos resultados para p
if posicoes_p:
    print(f"O valor {p} foi encontrado nas seguintes posições: {posicoes_p}")
else:
    print(f"O valor {p} não foi encontrado na lista.")

# Exibição dos resultados para v
if posicoes_v:
    print(f"O valor {v} foi encontrado nas seguintes posições: {posicoes_v}")
else:
    print(f"O valor {v} não foi encontrado na lista.")
