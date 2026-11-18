'''
Exercício 10.9 Crie classes para representar estados e cidades. Cada estado tem um
nome, sigla e cidades. Cada cidade tem nome e população. Escreva um programa de
testes que crie três estados com algumas cidades em cada um. Exiba a população
de cada estado como a soma da população de suas cidades.

'''


class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao


class Estado:
    def __init__(self, nome, sigla, cidades=None):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades if cidades is not None else []

    def adiciona_cidade(self, cidade):
        self.cidades.append(cidade)

    def populacao_total(self):
        return sum(cidade.populacao for cidade in self.cidades)


# --- Programa de Testes ---

# 1. Estado: São Paulo (SP)
sp = Estado("São Paulo", "SP", [
    Cidade("São Paulo", 11451245),
    Cidade("Campinas", 1138309),
    Cidade("Santos", 418608),
])

# 2. Estado: Rio de Janeiro (RJ)
rj = Estado("Rio de Janeiro", "RJ", [
    Cidade("Rio de Janeiro", 6211423),
    Cidade("Niterói", 481758),
    Cidade("Petrópolis", 278881),
])

# 3. Estado: Minas Gerais (MG)
mg = Estado("Minas Gerais", "MG", [
    Cidade("Belo Horizonte", 2315560),
    Cidade("Uberlândia", 713232),
    Cidade("Juiz de Fora", 540756),
])

# Lista com os estados para exibição
estados = [sp, rj, mg]

for estado in estados:
    total_habitantes = estado.populacao_total()
    print(f"Estado: {estado.nome} ({estado.sigla})")
    print(f"População total: {total_habitantes:,} habitantes".replace(",", "."))
    print("-" * 35)
