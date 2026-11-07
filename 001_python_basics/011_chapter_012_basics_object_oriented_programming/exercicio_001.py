'''
Exercício 10.1 Adicione os atributos tamanho e marca à classe Televisão. Crie
dois objetos Televisão e atribua tamanhos e marcas diferentes. Depois, imprima o
valor desses atributos de forma a confirmar a independência dos valores de cada
instância (objeto).

'''


class Televisão:
    def __init__(self, marca, tamanho):
        self.ligada = False
        self.canal = 2
        self.marca = marca
        self.tamanho = tamanho

# Criação de duas instâncias (objetos) com valores diferentes
tv_sala = Televisão("Samsung", 55)
tv_quarto = Televisão("LG", 32)

# Exibição dos atributos para comprovar a independência de cada objeto
print(f"TV da Sala: Marca = {tv_sala.marca}, Tamanho = {tv_sala.tamanho} polegadas")
print(f"TV do Quarto: Marca = {tv_quarto.marca}, Tamanho = {tv_quarto.tamanho} polegadas")
