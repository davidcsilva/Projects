'''
Escreva uma função que receba uma string e uma lista. A função
deve comparar a string passada com os elementos da lista, também passada como
parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso
em caso contrário.

'''


def busca_string(texto, lista):
    return texto in lista



frutas = ["maçã", "banana", "laranja", "uva"]

print(busca_string("banana", frutas))  # Retorna True
print(busca_string("abacaxi", frutas)) # Retorna False
