'''
Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
(())			OK
()()(()())
OK
())				Erro
'''

expressao = input("Digite a expressão com parênteses: ")

pilha = []
correto = True

for caractere in expressao:
    if caractere == "(":
        pilha.append("(")
    elif caractere == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            # Encontrou ')' sem nenhum '(' correspondente na pilha
            correto = False
            break

# Se a pilha não estiver vazia no final, sobrou '(' sem fechar
if len(pilha) > 0:
    correto = False

# Exibição do resultado
if correto:
    print("OK")
else:
    print("Erro")
