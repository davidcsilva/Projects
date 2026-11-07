'''
Modifique o programa da listagem 5.10 para que aceite respostas
com letras maiúsculas e minúsculas em todas as questões.
'''

pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ")

    if questao == 1 and resposta.lower() == "b":
        pontos = pontos + 1
    if questao == 2 and resposta.lower() == "a":
        pontos = pontos + 1
    if questao == 3 and resposta.lower() == "d":
        pontos = pontos + 1

    questao = questao + 1

print(f"O aluno deu {pontos} resposta(s) correta(s).")
