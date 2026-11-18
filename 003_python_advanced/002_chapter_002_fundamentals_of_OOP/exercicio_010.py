'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.10

Enunciado:
Projetar um diagrama de objetos que representa a estrutura de um carro.
Indicar as possíveis relações de associação, generalização e agregação.
'''

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# ==============================================================================
# 1. GENERALIZAÇÃO (Herança - Relação "É UM")
# ==============================================================================

class Veiculo(ABC):
    """
    Classe Base / Superclasse.
    Representa a generalização de qualquer veículo de transporte.
    """

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    @abstractmethod
    def acelerar(self) -> None:
        """Contrato abstrato que as subclasses devem especializar."""
        pass


class Motor(ABC):
    """Generalização abstrata de motores."""

    def __init__(self, potencia_cv: int) -> None:
        self.potencia_cv = potencia_cv

    @abstractmethod
    def tipo_combustivel(self) -> str:
        pass


class MotorCombustao(Motor):
    """Especialização: Motor a combustão (gasolina, etanol, diesel)."""

    def __init__(self, potencia_cv: int, cilindradas: float, combustivel: str = "Flex") -> None:
        super().__init__(potencia_cv)
        self.cilindradas = cilindradas
        self.combustivel = combustivel

    def tipo_combustivel(self) -> str:
        return f"Combustão ({self.combustivel} - {self.cilindradas:.1f}L)"


class MotorEletrico(Motor):
    """Especialização: Motor 100% elétrico."""

    def __init__(self, potencia_cv: int, capacidade_bateria_kwh: float) -> None:
        super().__init__(potencia_cv)
        self.capacidade_bateria_kwh = capacidade_bateria_kwh

    def tipo_combustivel(self) -> str:
        return f"Elétrico (Bateria {self.capacidade_bateria_kwh} kWh)"


# ==============================================================================
# 2. AGREGAÇÃO E COMPOSIÇÃO (Relação "TEM UM" / Parte-Todo)
# ==============================================================================

@dataclass
class Roda:
    """Componente Agregado: Rodas podem ser trocadas ou substituídas."""
    aro: int = 17
    pressao_psi: float = 32.0


@dataclass
class Chassi:
    """Componente Composto: O Chassi é a estrutura física inseparável do veículo."""
    numero_vin: str
    material: str = "Aço de Alta Resistência"


# ==============================================================================
# CLASSE CENTRAL: CARRO
# ==============================================================================

class Carro(Veiculo):
    """
    Representa o Carro completo, integrando:
    - Generalização: Carro É UM Veiculo.
    - Composição: Carro POSSUI UM Chassi (vital, inseparável).
    - Agregação: Carro POSSUI UM Motor e Rodas (podem ser substituídos/desacoplados).
    - Associação: Carro É CONDUZIDO POR um Motorista.
    """

    def __init__(
        self,
        marca: str,
        modelo: str,
        ano: int,
        numero_vin: str,
        motor: Motor,
        tamanho_aro: int = 17
    ) -> None:
        # Generalização: inicializa a superclasse Veiculo
        super().__init__(marca, modelo, ano)

        # COMPOSIÇÃO: O Chassi é criado junto e pertence exclusivamente a este carro
        self._chassi = Chassi(numero_vin=numero_vin)

        # AGREGAÇÃO: O Motor é injetado e pode ser substituído
        self.motor: Motor = motor

        # AGREGAÇÃO: As 4 rodas principais + 1 estepe
        self.rodas: list[Roda] = [Roda(aro=tamanho_aro) for _ in range(5)]

        # ASSOCIAÇÃO: Referência fraca/independente para o motorista atual
        self.motorista_atual: "Motorista | None" = None

    @property
    def chassi(self) -> Chassi:
        return self._chassi

    def acelerar(self) -> None:
        if not self.ligado:
            print(f"[{self.modelo}] Não é possível acelerar com o carro desligado.")
            return
        print(f"[{self.modelo}] Acelerando com motor {self.motor.tipo_combustivel()} ({self.motor.potencia_cv} cv)!")

    def ligar(self) -> None:
        if self.motorista_atual is None:
            print(f"[{self.modelo}] Aviso: Carro ligado sem motorista associado.")
        self.ligado = True
        print(f"[{self.modelo}] Motor ligado!")

    def desligar(self) -> None:
        self.ligado = False
        print(f"[{self.modelo}] Carro desligado.")

    # ASSOCIAÇÃO: Estabelece vínculo com outro objeto independente (Motorista)
    def associar_motorista(self, motorista: "Motorista") -> None:
        self.motorista_atual = motorista
        print(f"[{self.modelo}] Motorista {motorista.nome} assumiu o volante.")

    def desassociar_motorista(self) -> None:
        if self.motorista_atual:
            print(
                f"[{self.modelo}] Motorista {self.motorista_atual.nome} saiu do carro.")
            self.motorista_atual = None


# ==============================================================================
# 3. ASSOCIAÇÃO (Relação de Uso / Interação entre Objetos Independentes)
# ==============================================================================

@dataclass
class Motorista:
    """
    Representa a pessoa habilitada.
    Existe independentemente de qualquer carro específico (relação de Associação).
    """
    nome: str
    cnh: str

    def dirigir(self, carro: Carro) -> None:
        carro.associar_motorista(self)
        carro.ligar()
        carro.acelerar()


# ==============================================================================
# Demonstração Prática da Estrutura
# ==============================================================================
if __name__ == "__main__":
    print("=== Estrutura de Objetos do Carro ===")

    # 1. Criando Motor (Agregação) e Chassi interno (Composição)
    motor_turbo = MotorCombustao(
        potencia_cv=185, cilindradas=1.3, combustivel="Flex")
    meu_carro = Carro(
        marca="Jeep",
        modelo="Compass",
        ano=2026,
        numero_vin="9BRJ999888777666",
        motor=motor_turbo,
        tamanho_aro=18
    )

    print(
        f"\nCarro Criado: {meu_carro.marca} {meu_carro.modelo} ({meu_carro.ano})")
    print(f"- [Generalização] É um Veículo")
    print(f"- [Composição]    Chassi VIN: {meu_carro.chassi.numero_vin}")
    print(f"- [Agregação]     Motor: {meu_carro.motor.tipo_combustivel()}")
    print(
        f"- [Agregação]     Quantidade de Rodas: {len(meu_carro.rodas)} (Aro {meu_carro.rodas[0].aro})")

    # 2. Associação com Motorista
    print("\n--- Associação com Motorista ---")
    condutor = Motorista(nome="David Costa", cnh="123456789-00")
    condutor.dirigir(meu_carro)

    meu_carro.desligar()
    meu_carro.desassociar_motorista()
