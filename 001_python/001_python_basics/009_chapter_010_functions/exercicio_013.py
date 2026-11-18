'''
Altere o programa da listagem 8.37 de forma que o usuário tenha
três chances de acertar o número. O programa termina se o usuário acertar ou
errar três vezes.

'''


import random

numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    chute = int(input("Adivinhe o número (1 a 10): "))
    
    if chute == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Número incorreto! Você ainda tem {tentativas} chance(s).")
        else:
            print(f"Você errou 3 vezes. Fim de jogo! O número era {numero_secreto}.")


