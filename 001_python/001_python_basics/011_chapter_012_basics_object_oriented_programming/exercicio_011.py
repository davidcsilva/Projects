'''
Exercício 10.11 Altere a classe ContaEspecial de forma que seu extrato exiba o limite
e o total disponível para saque.

'''


class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC Número: {self.número} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC Nº {self.número}")
        for op in self.operações:
            print(f"{op[0]:10s} {op[1]:10.2f}")
        print(f"\n       Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            return False

    def extrato(self):
        print(f"Extrato CC Especial Nº {self.número}")
        for op in self.operações:
            print(f"{op[0]:10s} {op[1]:10.2f}")
        
        disponivel = self.saldo + self.limite
        print(f"\n       Saldo: {self.saldo:10.2f}")
        print(f"      Limite: {self.limite:10.2f}")
        print(f"  Disponível: {disponivel:10.2f}\n")
