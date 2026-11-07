'''
Exercício 10.4 Utilizando o que aprendemos com funções, modifique o construtor
da classe Televisão de forma que min e max sejam parâmetros opcionais, onde min
vale 2 e max vale 14, caso outro valor não seja passado.

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
