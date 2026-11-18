'''
Exercício 10.5 Utilizando a classe Televisão modificada no exercício anterior, crie
duas instâncias (objetos), especificando o valor de min e max por nome.

'''


class Televisão:
    def __init__(self, canal_inicial=2, min=2, max=14):
        self.ligada = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax


# Instância 1: passando min e max explicitamente por nome
tv1 = Televisão(canal_inicial=3, min=1, max=30)

# Instância 2: passando min e max por nome em ordem diferente e aproveitando o canal_inicial padrão
tv2 = Televisão(max=60, min=4)

# Exibição dos atributos de cada objeto
print(f"TV 1: canal={tv1.canal}, canal mínimo={tv1.cmin}, canal máximo={tv1.cmax}")
print(f"TV 2: canal={tv2.canal}, canal mínimo={tv2.cmin}, canal máximo={tv2.cmax}")
