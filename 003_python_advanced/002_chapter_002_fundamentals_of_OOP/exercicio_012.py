'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.12

Enunciado:
Construir uma classe Pessoa com as funções membro e atributos que criam oportunos.
'''

from datetime import date
from enum import Enum


class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro(a)"
    CASADO = "Casado(a)"
    DIVORCIADO = "Divorciado(a)"
    VIUVO = "Viúvo(a)"


class Pessoa:
    """
    Representa uma pessoa com dados cadastrais, biométricos e relacionais.

    Atributos encapsulados:
    - Identificação: nome, cpf, data_nascimento, sexo
    - Biometria: peso_kg, altura_m
    - Contato: email, telefone
    - Estado Civil e Cônjuge

    Funções membro / Métodos:
    - Cálculo dinâmico de idade (baseado na data atual)
    - Cálculo e classificação de IMC (Índice de Massa Corporal)
    - Verificação de maioridade
    - Comportamentos: fazer aniversário, engordar, emagrecer, crescer, casar
    - Apresentação e exibição de ficha cadastral
    """

    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: date,
        sexo: str = "Não informado",
        peso_kg: float = 70.0,
        altura_m: float = 1.75,
        email: str = "",
        telefone: str = ""
    ) -> None:
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        if peso_kg <= 0 or altura_m <= 0:
            raise ValueError(
                "Peso e altura devem ser valores estritamente positivos.")

        self._nome: str = nome.strip()
        self._cpf: str = cpf.strip()
        self._data_nascimento: date = data_nascimento
        self.sexo: str = sexo
        self._peso_kg: float = float(peso_kg)
        self._altura_m: float = float(altura_m)
        self.email: str = email
        self.telefone: str = telefone

        # Estado relacional
        self.estado_civil: EstadoCivil = EstadoCivil.SOLTEIRO
        self.conjuge: "Pessoa | None" = None

    # --------------------------------------------------------------------------
    # Getters / Setters e Propriedades Calculadas
    # --------------------------------------------------------------------------
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento

    @property
    def peso_kg(self) -> float:
        return self._peso_kg

    @property
    def altura_m(self) -> float:
        return self._altura_m

    @property
    def idade(self) -> int:
        """
        Calcula a idade exata com base na data de nascimento e data atual.
        A idade não deve ser atributo estático pois varia com o tempo.
        """
        hoje = date.today()
        anos = hoje.year - self._data_nascimento.year
        # Se ainda não fez aniversário no ano corrente, subtrai 1 ano
        if (hoje.month, hoje.day) < (self._data_nascimento.month, self._data_nascimento.day):
            anos -= 1
        return max(0, anos)

    @property
    def maior_de_idade(self) -> bool:
        """Verifica se a pessoa atingiu a maioridade civil (>= 18 anos)."""
        return self.idade >= 18

    @property
    def imc(self) -> float:
        """Calcula o Índice de Massa Corporal: peso / (altura ^ 2)."""
        return self._peso_kg / (self._altura_m ** 2)

    @property
    def classificacao_imc(self) -> str:
        """Classifica o IMC de acordo com as diretrizes da OMS."""
        valor = self.imc
        if valor < 18.5:
            return "Abaixo do peso"
        elif valor < 24.9:
            return "Peso normal / Eutrofia"
        elif valor < 29.9:
            return "Sobrepeso"
        elif valor < 34.9:
            return "Obesidade Grau I"
        elif valor < 39.9:
            return "Obesidade Grau II"
        return "Obesidade Grau III (Mórbida)"

    # --------------------------------------------------------------------------
    # Funções Membro de Comportamento e Mudança de Estado
    # --------------------------------------------------------------------------
    def engordar(self, quilos: float) -> None:
        """Aumenta o peso corporal da pessoa."""
        if quilos <= 0:
            raise ValueError("O valor de ganho de peso deve ser positivo.")
        self._peso_kg += quilos
        print(
            f"[{self.nome}] Ganhou {quilos:.1f} kg. Novo peso: {self._peso_kg:.1f} kg.")

    def emagrecer(self, quilos: float) -> None:
        """Reduz o peso corporal da pessoa de forma segura."""
        if quilos <= 0:
            raise ValueError("O valor de perda de peso deve ser positivo.")
        if self._peso_kg - quilos < 20:
            raise ValueError(
                "Operação inválida: peso resultante incompatível com a vida.")
        self._peso_kg -= quilos
        print(
            f"[{self.nome}] Perdeu {quilos:.1f} kg. Novo peso: {self._peso_kg:.1f} kg.")

    def crescer(self, centimetros: float) -> None:
        """Aumenta a altura da pessoa em centímetros."""
        if centimetros <= 0:
            raise ValueError("O crescimento deve ser positivo.")
        self._altura_m += (centimetros / 100.0)
        print(
            f"[{self.nome}] Cresceu {centimetros:.1f} cm. Nova altura: {self._altura_m:.2f} m.")

    def casar_com(self, outra_pessoa: "Pessoa") -> None:
        """
        Estabelece a união matrimonial mútua entre duas instâncias de Pessoa.
        """
        if self is outra_pessoa:
            raise ValueError("Uma pessoa não pode casar consigo mesma.")
        if not self.maior_de_idade or not outra_pessoa.maior_de_idade:
            raise ValueError(
                "Ambas as pessoas devem ser maiores de idade para casar.")

        self.estado_civil = EstadoCivil.CASADO
        self.conjuge = outra_pessoa

        outra_pessoa.estado_civil = EstadoCivil.CASADO
        outra_pessoa.conjuge = self

        print(
            f"\n[Casamento Realizado!] {self.nome} casou-se com {outra_pessoa.nome}!")

    def apresentar_se(self) -> str:
        """Retorna uma apresentação cordial em primeira pessoa."""
        return (
            f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos, "
            f"meço {self.altura_m:.2f}m e peso {self.peso_kg:.1f}kg."
        )

    def exibir_ficha_completa(self) -> None:
        """Imprime o relatório cadastral detalhado da pessoa."""
        conjuge_nome = self.conjuge.nome if self.conjuge else "Nenhum"
        maioridade = "Sim" if self.maior_de_idade else "Não"

        print("\n" + "=" * 55)
        print(f"FICHA CADASTRAL: {self.nome.upper()}")
        print("=" * 55)
        print(f"CPF:             {self.cpf}")
        print(
            f"Nascimento:      {self.data_nascimento.strftime('%d/%m/%Y')} ({self.idade} anos)")
        print(f"Maior de Idade:  {maioridade}")
        print(f"Sexo:            {self.sexo}")
        print(
            f"Estado Civil:    {self.estado_civil.value} (Cônjuge: {conjuge_nome})")
        print(
            f"Altura:          {self.altura_m:.2f} m | Peso: {self.peso_kg:.1f} kg")
        print(
            f"IMC:             {self.imc:.2f} kg/m² ({self.classificacao_imc})")
        if self.email:
            print(f"E-mail:          {self.email}")
        if self.telefone:
            print(f"Telefone:        {self.telefone}")
        print("=" * 55)

    def __str__(self) -> str:
        return f"{self.nome} ({self.idade} anos, {self.estado_civil.value})"

    def __repr__(self) -> str:
        return f"Pessoa(nome='{self.nome}', cpf='{self.cpf}', idade={self.idade})"


# ==============================================================================
# Demonstração Prática de Uso
# ==============================================================================
if __name__ == "__main__":
    p1 = Pessoa(
        nome="David Costa",
        cpf="123.456.789-00",
        data_nascimento=date(1995, 8, 20),
        sexo="Masculino",
        peso_kg=80.0,
        altura_m=1.82,
        email="david.costa@email.com",
        telefone="(11) 98765-4321"
    )

    p2 = Pessoa(
        nome="Mariana Lima",
        cpf="987.654.321-99",
        data_nascimento=date(1998, 3, 15),
        sexo="Feminino",
        peso_kg=62.0,
        altura_m=1.68,
        email="mariana.lima@email.com",
        telefone="(11) 91234-5678"
    )

    # 1. Apresentação inicial
    print(p1.apresentar_se())
    print(p2.apresentar_se())

    # 2. Exibição de ficha cadastral
    p1.exibir_ficha_completa()

    # 3. Teste de mudanças de estado físico
    print("\n--- Alterações de Estado Físico ---")
    p1.emagrecer(3.5)
    p1.crescer(1.0)
    print(f"Novo IMC de {p1.nome}: {p1.imc:.2f} ({p1.classificacao_imc})")

    # 4. Relação entre instâncias (Casamento)
    p1.casar_com(p2)
    p1.exibir_ficha_completa()
