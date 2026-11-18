'''
Exercício 10.2 Atualmente, a classe Televisão inicializa o canal com 2. Modifique
a classe Televisão de forma a receber o canal inicial em seu construtor.

'''



class Televisão:
    def __init__(self, canal_inicial, min_canal=1, max_canal=99):
        self.ligada = False
        self.canal = canal_inicial
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

# Criação de instâncias com canais iniciais diferentes
tv1 = Televisão(canal_inicial=4)
tv2 = Televisão(canal_inicial=10)

print(f"Canal inicial da TV 1: {tv1.canal}")
print(f"Canal inicial da TV 2: {tv2.canal}")
