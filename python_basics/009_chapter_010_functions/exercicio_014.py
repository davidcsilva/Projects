'''
Altere o programa da listagem 7.45, o jogo da forca. Escolha a palavra
a adivinhar utilizando números aleatórios.

'''


import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "computador", "desenvolvimento", "algoritmo"]

# Escolhe uma palavra aleatoriamente da lista
palavra = palavras[random.randint(0, len(palavras) - 1)].lower()

# Também poderia ser usado: palavra = random.choice(palavras).lower()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    
    print(f"\nPalavra: {senha}")
    
    if senha == palavra:
        print("Você acertou!")
        break
        
    tentativa = input("\nDigite uma letra: ").lower().strip()
    
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas.append(tentativa)
        if tentativa in palavra:
            acertos.append(tentativa)
        else:
            erros += 1
            print("Você errou!")
            
    print("X==:==")
    print("X  :  ")
    print(f"X  {'O' if erros >= 1 else ''}")
    print(f"X {'/|\\' if erros >= 2 else ''}")
    print(f"X {'/ \\' if erros >= 3 else ''}")
    print("X     ")
    print("===========")
    
    if erros == 3:
        print(f"Enforcado! A palavra era: {palavra}")
        break
