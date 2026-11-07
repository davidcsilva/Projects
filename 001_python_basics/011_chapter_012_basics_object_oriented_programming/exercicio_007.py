'''
Exercício 10.7 Modifique o método resumo da classe Conta para exibir o nome e
o telefone de cada cliente.

'''



class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número

    def resumo(self):
        print(f"CC Número: {self.número} | Saldo: R${self.saldo:10.2f}")
        print("Clientes:")
        for cliente in self.clientes:
            print(f"  Nome: {cliente.nome} - Telefone: {cliente.telefone}")
        print("-" * 40)

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
        self.saldo += valor
