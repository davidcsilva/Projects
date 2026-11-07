'''
Exercício 10.12 Observe o método saque das classes Conta e ContaEspecial. Modifique
o método saque da classe Conta de forma que a verificação da possibilidade
de saque seja feita por um novo método, substituindo a condição atual. Esse
novo método retornará verdadeiro se o saque puder ser efetuado, e falso em caso
contrário. Modifique a classe ContaEspecial de forma a trabalhar com esse novo
método. Verifique se você ainda precisa trocar o método saque de ContaEspecial
ou apenas o novo método criado para verificar a possibilidade de saque.

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

    def pode_sacar(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        if self.pode_sacar(valor):
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
        super().__init__(clientes, número, saldo)
        self.limite = limite

    def pode_sacar(self, valor):
        return self.saldo + self.limite >= valor

    def extrato(self):
        print(f"Extrato CC Especial Nº {self.número}")
        for op in self.operações:
            print(f"{op[0]:10s} {op[1]:10.2f}")
        disponivel = self.saldo + self.limite
        print(f"\n       Saldo: {self.saldo:10.2f}")
        print(f"      Limite: {self.limite:10.2f}")
        print(f"  Disponível: {disponivel:10.2f}\n")
