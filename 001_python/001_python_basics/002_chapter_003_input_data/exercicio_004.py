'''
Escreva uma expressão para determinar se uma pessoa deve ou não
pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
R$ 1.200,00.
'''

import _collections_abc
salario = float(input("Digite o seu salário: "))

if salario > 1200:
    print("Deve pagar imposto")
else:
    print("Não deve pagar imposto")
