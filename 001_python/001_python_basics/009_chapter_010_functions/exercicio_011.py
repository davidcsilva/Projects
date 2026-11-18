'''
Escreva uma função para validar uma variável string. Essa função
recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne
verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo,
e falso em caso contrário.

'''


def valida_string(texto, minimo, maximo):
    tamanho = len(texto)
    return minimo <= tamanho <= maximo



print(valida_string("Python", 2, 10))  # Retorna True (tamanho 6)
print(valida_string("A", 2, 5))        # Retorna False (tamanho 1)
print(valida_string("Opção", 5, 5))     # Retorna True (tamanho exacto 5)
print(valida_string("Teste", 1, 3))     # Retorna False (tamanho 5)
