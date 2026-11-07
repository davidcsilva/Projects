'''
Faça um programa que percorra duas listas e gere uma terceira sem
elementos repetidos.
'''

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

lista3 = lista1 + lista2
lista3 = list(set(lista3))

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3 (combinada): {lista3}")
