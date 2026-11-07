'''
Exercício 10.3 Modifique a classe Televisão de forma que, se pedirmos para mudar
o canal para baixo, além do mínimo, ela vá para o canal máximo. Se mudarmos
para cima, além do canal máximo, que volte ao canal mínimo. Exemplo:
> > > tv=Televisão(2,10)
> > > tv.muda_canal_para_baixo()
> > > tv.canal
10
> > > tv.muda_canal_para_cima()
> > > tv.canal
2

'''



class Televisão:
    def __init__(self, min_canal, max_canal):
        self.ligada = False
        self.canal = min_canal
        self.cmin = min_canal
        self.cmax = max_canal

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
