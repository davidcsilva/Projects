'''
Modifique o programa abaixo usando for. Explique por
que nem todos os while podem ser transformados em for.

L=[]
while True:
n=int(input("Digite um número (0 sai):"))
if n == 0:
		break
L.append(n)
x=0
while x < len(L):
print(L[x])
x=x+1


'''

L = []

# Como não sabemos a quantidade prévia de entradas, usamos iter() com o valor sentinela 0
for n in iter(lambda: int(input("Digite um número (0 sai): ")), 0):
    L.append(n)

# Para percorrer os elementos de uma lista, o 'for' substitui diretamente o segundo 'while'
for elemento in L:
    print(elemento)
