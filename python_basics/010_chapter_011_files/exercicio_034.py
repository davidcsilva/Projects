'''
Exercício 9.34 Altere o programa da listagem 7.45, o jogo da forca. Dessa vez,
utilize as funções de tempo para cronometrar a duração das partidas.


'''

import random
import time

palavras = ["abacaxi", "banana", "laranja", "morango", "melancia", "uva"]

palavra = random.choice(palavras).lower()
digitadas = []
acertos = []
erros = 0

print("--- JOGO DA FORCA ---")

# Inicia a contagem do tempo da partida
tempo_inicio = time.time()

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(f"\nPalavra: {senha}")

    if senha == palavra:
        print("\nVocê acertou!")
        break

    tentativa = input("Digite uma letra: ").lower().strip()

    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma única letra válida.")
        continue

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue

    digitadas.append(tentativa)

    if tentativa in palavra:
        acertos.append(tentativa)
    else:
        erros += 1
        print("Você errou!")
        print("X==:==")
        print("X  :  ")
        if erros >= 1:
            print("X  O  ")
        else:
            print("X")
        if erros == 2:
            print("X  |  ")
        elif erros == 3:
            print("X \\|  ")
        elif erros >= 4:
            print("X \\|/ ")
        else:
            print("X")
        if erros == 5:
            print("X /   ")
        elif erros >= 6:
            print("X / \\ ")
        else:
            print("X")
        print("X\n=======")

        if erros == 6:
            print(f"\nEnforcado! A palavra secreta era '{palavra}'.")
            break

# Finaliza a contagem do tempo
tempo_fim = time.time()
duracao = tempo_fim - tempo_inicio

minutos = int(duracao // 60)
segundos = duracao % 60

print(
    f"\nDuração da partida: {duracao:.2f} segundos ({minutos} min e {segundos:.1f} s).")
