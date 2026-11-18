'''
Modifique o programa para utilizar listas de strings para desenhar
o boneco da forca. Você pode utilizar uma lista para cada linha e organizá-las em
uma lista de listas. Em vez de controlar quando imprimir cada parte, desenhe
nessas listas, substituindo o elemento a desenhar.
Exemplo:
>>> linha = list("X------")
>>> linha
['X', '-', '-', '-', '-', '-', '-']
>>> linha[6] = "|"
>>> linha
['X', '-', '-', '-', '-', '-', '|']
>>> "".join(linha)
'X-----|'

'''

# Lista de palavras disponíveis
lista_de_palavras = [
    "python",
    "programacao",
    "computador",
    "algoritmo",
    "dicionario",
    "variavel",
    "desenvolvimento"
]

numero = int(input("Digite um número para escolher a palavra secreta: "))
indice = (numero * 776) % len(lista_de_palavras)
palavra = lista_de_palavras[indice]

# Limpa a tela
for _ in range(100):
    print()

# Representação inicial da forca vazia como listas de caracteres
forca = [
    list("X==:=="),
    list("X  : "),
    list("X    "),  # Posição [2][3] -> Cabeça 'O'
    # Posição [3][2], [3][3], [3][4] -> Tronco e braços '\', '|', '/'
    list("X    "),
    list("X    "),  # Posição [4][2], [4][4] -> Pernas '/', '\'
    list("X\n===========")
]

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

            # Desenha a parte do corpo correspondente ao número do erro
            if erros == 1:
                forca[2][3] = "O"        # Cabeça
            elif erros == 2:
                forca[3][3] = "|"        # Tronco
            elif erros == 3:
                forca[3][2] = "\\"       # Braço esquerdo
            elif erros == 4:
                forca[3][4] = "/"        # Braço direito
            elif erros == 5:
                forca[4][2] = "/"        # Perna esquerda
            elif erros == 6:
                forca[4][4] = "\\"       # Perna direita

    # Imprime a matriz da forca convertendo cada linha de lista para string
    for linha in forca:
        print("".join(linha))

    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
