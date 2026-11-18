'''
Modifique o jogo da forca de forma a utilizar uma lista de palavras.
No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula:
índice = (número * 776) % len(lista_de_palavras).
'''

# Lista de palavras disponíveis para o jogo
lista_de_palavras = [
    "python",
    "programacao",
    "computador",
    "algoritmo",
    "dicionario",
    "variavel",
    "desenvolvimento"
]

# Solicita o número para calcular o índice
numero = int(input("Digite um número para escolher a palavra secreta: "))

# Cálculo do índice conforme a fórmula fornecida
indice = (numero * 776) % len(lista_de_palavras)
palavra = lista_de_palavras[indice]

# Limpa a tela para iniciar o jogo
for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

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

    # Desenho da Forca
    print("X==:==")
    print("X  : ")
    print("X  O " if erros >= 1 else "X")

    linha2 = ""
    if erros == 2:
        linha2 = "  | "
    elif erros == 3:
        linha2 = " \\| "
    elif erros >= 4:
        linha2 = " \\|/ "
    print("X%s" % linha2)

    linha3 = ""
    if erros == 5:
        linha3 = " /  "
    elif erros >= 6:
        linha3 = " / \\ "
    print("X%s" % linha3)

    print("X\n===========")

    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
