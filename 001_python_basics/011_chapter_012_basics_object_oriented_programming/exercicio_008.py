'''
Exercício 10.8 Crie uma nova conta, agora tendo João e José como clientes e saldo
igual a 500.


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


# 1. Criação dos objetos Cliente
joao = Cliente("João da Silva", "7777-3333")
jose = Cliente("José de Souza", "8888-4444")

# 2. Criação da nova Conta com os dois clientes e saldo igual a 500
conta_joao_jose = Conta(clientes=[joao, jose], número="9876-1", saldo=500)

# 3. Exibição do resumo da conta criada
conta_joao_jose.resumo()
