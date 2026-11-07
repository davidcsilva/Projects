'''
Exercício 10.6 Altere o programa de forma que a mensagem saldo insuficiente seja
exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível.

'''


class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número

    def resumo(self):
        print(f"CC Número: {self.número} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
        self.saldo += valor
