'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 5.1

Enunciado:
Descreva e justifique os objetos que são obtidos em cada um destes casos:
a) Os habitantes da Europa e seus endereços postais.
b) Os clientes de um banco que têm um cofre alugado.
c) Os endereços de correio eletrônico de uma universidade.
d) Os empregados de uma empresa e suas chaves de acesso aos sistemas de segurança.
'''

from dataclasses import dataclass, field


# ==============================================================================
# a) Os habitantes da Europa e seus endereços postais
# ==============================================================================
# Descrição e Justificativa:
# - Objetos de Domínio: 'Habitante' e 'EnderecoPostal'.
# - Relação / Cardinalidade: Muitos-para-Um (N:1).
#   Vários habitantes podem partilhar o mesmo endereço postal (ex.: membros da
#   mesma família residentes na mesma habitação). Cada habitante possui um endereço.
# - Estrutura Computacional: Mapeamento / Dicionário (dict[Habitante, EnderecoPostal]).
#   Matematicamente, comporta-se como uma função não-injetora (valores repetidos).

@dataclass(frozen=True)
class EnderecoPostal:
    rua: str
    numero: str
    codigo_postal: str
    cidade: str
    pais: str


@dataclass(frozen=True)
class Habitante:
    id_cidadao: str
    nome: str


# ==============================================================================
# b) Os clientes de um banco que têm um cofre alugado
# ==============================================================================
# Descrição e Justificativa:
# - Objetos de Domínio: 'Cliente' e 'Cofre'.
# - Relação / Cardinalidade: Um-para-Um (1:1) ou Um-para-Muitos (1:N).
#   O enunciado restringe ao subconjunto de clientes que possuem cofre. Cada cofre
#   alugado pertence exclusivamente a um titular (ou cotitulares).
# - Estrutura Computacional:
#   1) Subconjunto filtrado: set[Cliente] (apenas clientes com contrato de cofre ativo).
#   2) Mapeamento injetivo: dict[Cofre, Cliente] ou dict[Cliente, Cofre].

@dataclass(frozen=True)
class Cliente:
    id_cliente: str
    nome: str


@dataclass(frozen=True)
class Cofre:
    numero_cofre: int
    agencia: str


# ==============================================================================
# c) Os endereços de correio eletrônico de uma universidade
# ==============================================================================
# Descrição e Justificativa:
# - Objetos de Domínio: 'EnderecoEmail' (ou instâncias de 'str').
# - Relação / Cardinalidade: Coleção unária de elementos atômicos homogêneos.
# - Estrutura Computacional: Conjunto (set[str]).
#   Justificativa da Unicidade: Endereços de e-mail institucionais são estritamente
#   únicos (não podem existir duplicatas no mesmo domínio). A ordem dos elementos
#   não é relevante para sua existência no diretório do servidor.

universidade_emails: set[str] = {
    "aluno1@universidade.pt",
    "professor2@universidade.pt",
    "reitoria@universidade.pt"
}


# ==============================================================================
# d) Os empregados de uma empresa e suas chaves de acesso aos sistemas de segurança
# ==============================================================================
# Descrição e Justificativa:
# - Objetos de Domínio: 'Empregado' e 'ChaveAcesso'.
# - Relação / Cardinalidade: Muitos-para-Muitos (N:M).
#   Um empregado pode ter múltiplas chaves (ex.: porta principal, datacenter, cofre).
#   Uma mesma chave/permissão de acesso pode ser concedida a múltiplos empregados.
# - Estrutura Computacional: Multimapa ou Dicionário com conjuntos de valores
#   (dict[Empregado, set[ChaveAcesso]]).

@dataclass(frozen=True)
class ChaveAcesso:
    id_chave: str
    nivel_permissao: str
    sala_ou_sistema: str


@dataclass
class Empregado:
    matricula: str
    nome: str
    chaves_acesso: set[ChaveAcesso] = field(default_factory=set)

    def conceder_chave(self, chave: ChaveAcesso) -> None:
        self.chaves_acesso.add(chave)


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    print("--- Caso a: Habitantes e Endereços ---")
    end_lisboa = EnderecoPostal(
        "Av. da Liberdade", "100", "1250-096", "Lisboa", "Portugal")
    h1 = Habitante("PT123", "Maria Silva")
    h2 = Habitante("PT456", "João Silva")
    habitantes_enderecos: dict[Habitante, EnderecoPostal] = {
        h1: end_lisboa, h2: end_lisboa}
    for hab, end in habitantes_enderecos.items():
        print(f"Habitante: {hab.nome} -> Endereço: {end.rua}, {end.cidade}")

    print("\n--- Caso b: Clientes com Cofre Alugado ---")
    c1 = Cliente("CLI001", "Ana Santos")
    cofre1 = Cofre(101, "Agência Central")
    cofres_alugados: dict[Cliente, Cofre] = {c1: cofre1}
    print(
        f"Cliente {c1.nome} possui o cofre #{cofres_alugados[c1].numero_cofre}")

    print("\n--- Caso c: Endereços de Correio Eletrônico ---")
    print(f"Total de emails únicos cadastrados: {len(universidade_emails)}")
    print(f"Emails: {universidade_emails}")

    print("\n--- Caso d: Empregados e Chaves de Acesso ---")
    chave_geral = ChaveAcesso("KEY-01", "Básico", "Entrada Principal")
    chave_ti = ChaveAcesso("KEY-02", "Avançado", "Data Center")

    emp1 = Empregado("EMP10", "Carlos Dev")
    emp1.conceder_chave(chave_geral)
    emp1.conceder_chave(chave_ti)

    emp2 = Empregado("EMP20", "Beatriz Admin")
    emp2.conceder_chave(chave_geral)

    for emp in [emp1, emp2]:
        chaves_str = ", ".join(c.sala_ou_sistema for c in emp.chaves_acesso)
        print(
            f"Empregado {emp.nome} ({emp.matricula}) tem acesso a: [{chaves_str}]")
