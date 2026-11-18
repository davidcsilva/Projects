'''
17.9 Projete a seguinte hierarquia de classes:
Pessoa
Nome
idade
visualizar()
Estudante
nome
idade
id
visualizar()
herdado
herdado
definido
redefinido
Professor
nome
idade
salário
visualizar
herdado
herdado
definido
herdado
Escreva um programa que manipule a hierarquia de classes, leia um objeto de cada classe e o visualize:
a) Sem utilizar funções virtuais.
b) Utilizando funções virtuais.
'''


class Pessoa:
    def __init__(self, nome: str = "", idade: int = 0):
        self.nome = nome
        self.idade = idade

    def ler(self) -> None:
        self.nome = input("Nome: ")
        self.idade = int(input("Idade: "))

    def visualizar(self) -> None:
        print(f"[Pessoa] Nome: {self.nome} | Idade: {self.idade} anos")


class Estudante(Pessoa):
    def __init__(self, nome: str = "", idade: int = 0, id_estudante: str = ""):
        super().__init__(nome, idade)
        self.id = id_estudante

    def ler(self) -> None:
        super().ler()
        self.id = input("ID (Matrícula): ")

    # Redefine visualizar()
    def visualizar(self) -> None:
        print(
            f"[Estudante] Nome: {self.nome} | Idade: {self.idade} anos | ID: {self.id}")


class Professor(Pessoa):
    def __init__(self, nome: str = "", idade: int = 0, salario: float = 0.0):
        super().__init__(nome, idade)
        self.salario = salario

    def ler(self) -> None:
        super().ler()
        self.salario = float(input("Salário: R$ "))

    # Não redefine visualizar(): herda diretamente Pessoa.visualizar()


# ==============================================================================
# PROGRAMA PRINCIPAL: LEITURA E DEMONSTRAÇÃO DOS ITENS (a) E (b)
# ==============================================================================

if __name__ == "__main__":
    p = Pessoa()
    e = Estudante()
    prof = Professor()

    print("=== Leitura dos Dados ===")
    print("\n-- Dados de Pessoa --")
    p.ler()

    print("\n-- Dados de Estudante --")
    e.ler()

    print("\n-- Dados de Professor --")
    prof.ler()

    # Lista polimórfica contendo objetos da hierarquia Pessoa
    lista: list[Pessoa] = [p, e, prof]

    # --------------------------------------------------------------------------
    # a) Sem utilizar funções virtuais (forçando ligação estática à classe base)
    # --------------------------------------------------------------------------
    print("\n=== (a) Sem funções virtuais (chamada estática via Pessoa.visualizar) ===")
    for item in lista:
        # Ignora a redefinição em Estudante e executa sempre o método da classe base
        Pessoa.visualizar(item)

    # --------------------------------------------------------------------------
    # b) Utilizando funções virtuais (comportamento polimórfico padrão do Python)
    # --------------------------------------------------------------------------
    print("\n=== (b) Com funções virtuais (despacho dinâmico padrão do Python) ===")
    for item in lista:
        # Resolve dinamicamente:
        # - Pessoa    -> Pessoa.visualizar()
        # - Estudante -> Estudante.visualizar() (redefinido, mostra o ID)
        # - Professor -> Pessoa.visualizar()    (herdado)
        item.visualizar()
