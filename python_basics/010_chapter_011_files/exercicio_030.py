'''
Exercício 9.30 Modifique o programa da listagem 9.10 para gerar uma lista html,
usando os elementos ul e li. Todos os elementos da lista devem estar dentro do
elemento ul, e cada item dentro de um elemento li. Exemplo:
<ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>

'''
# Modificação da Listagem 9.10 para gerar uma lista HTML com <ul> e <li> (Exercício 9.30)

filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "O Grande Ditador"],
    "policial": ["Chinatown", "Fargo"],
    "guerra": ["Círculo de Fogo", "Platoon"],
}

with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("<!DOCTYPE html>\n")
    pagina.write('<html lang="pt-BR">\n')
    pagina.write("<head>\n")
    pagina.write('<meta charset="utf-8">\n')
    pagina.write("<title>Filmes</title>\n")
    pagina.write("</head>\n")
    pagina.write("<body>\n")

    for genero, lista_filmes in filmes.items():
        pagina.write(f"<h1>{genero}</h1>\n")
        pagina.write("<ul>\n")
        for filme in lista_filmes:
            pagina.write(f"  <li>{filme}</li>\n")
        pagina.write("</ul>\n")

    pagina.write("</body>\n")
    pagina.write("</html>\n")
