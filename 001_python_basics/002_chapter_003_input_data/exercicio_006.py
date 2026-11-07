'''
Escreva uma expressão que será utilizada para decidir se um aluno foi
ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores
que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
'''


materia_1 = float(input("Digite a nota da matéria 1: "))
materia_2 = float(input("Digite a nota da matéria 2: "))
materia_3 = float(input("Digite a nota da matéria 3: "))

if materia_1 > 7 and materia_2 > 7 and materia_3 > 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
