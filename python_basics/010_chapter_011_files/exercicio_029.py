'''
Exercício 9.29 Modifique o programa da listagem 9.10 para utilizar o elemento p
em vez de h2 nos filmes.

'''
# Modificação da Listagem 9.10 para utilizar <p> em vez de <h2> nos filmes (Exercício 9.29)

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

    for c, v in filmes.items():
        pagina.write(f"<h1>{c}</h1>\n")
        for e in v:
            # Alteração do Exercício 9.29: <p> em vez de <h2>
            pagina.write(f"<p>{e}</p>\n")

    pagina.write("</body>\n")
    pagina.write("</html>\n")
