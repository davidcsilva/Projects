'''
Capítulo 2: Fundamentos de POO (Programação Orientada a Objetos)
Exercício 15.11

Enunciado:
Projetar diagramas de objetos que representem a hierarquia de objetos do modelo Figura.
'''

from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


# ==============================================================================
# COMPONENTE DE APOIO: PONTO (Coordenada cartesiana)
# ==============================================================================

@dataclass
class Ponto:
    """Representa a coordenada espacial ou de tela de uma figura."""
    x: float = 0.0
    y: float = 0.0

    def __str__(self) -> str:
        return f"({self.x:.1f}, {self.y:.1f})"


# ==============================================================================
# 1. SUPERCLASSE ABSTRATA: FIGURA
# ==============================================================================

class Figura(ABC):
    """
    Superclasse abstrata que define o modelo genérico de uma figura geométrica.
    Define atributos universais como posição e cor, e estabelece o contrato
    polimórfico de cálculo de área, perímetro e desenho.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0, cor_preenchimento: str = "branco", cor_borda: str = "preto") -> None:
        self.posicao: Ponto = Ponto(x, y)
        self.cor_preenchimento: str = cor_preenchimento
        self.cor_borda: str = cor_borda

    @abstractmethod
    def calcular_area(self) -> float:
        """Contrato polimórfico para cálculo da área."""
        pass

    @abstractmethod
    def calcular_perimetro(self) -> float:
        """Contrato polimórfico para cálculo do perímetro / perímetro de borda."""
        pass

    def mover(self, delta_x: float, delta_y: float) -> None:
        """Move a figura no plano cartesiano."""
        self.posicao.x += delta_x
        self.posicao.y += delta_y
        print(f"[{self.__class__.__name__}] Movido para {self.posicao}.")

    @abstractmethod
    def descrever(self) -> None:
        """Exibe os dados detalhados da figura."""
        pass


# ==============================================================================
# 2. HIERARQUIA DE FIGURAS BIDIMENSIONAIS (PLANAS)
# ==============================================================================

class Circulo(Figura):
    """Especialização: Círculo (definido por seu raio)."""

    def __init__(self, raio: float, x: float = 0.0, y: float = 0.0, cor: str = "vermelho") -> None:
        super().__init__(x, y, cor_preenchimento=cor)
        if raio <= 0:
            raise ValueError("O raio deve ser estritamente positivo.")
        self.raio: float = raio

    def calcular_area(self) -> float:
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.raio

    def descrever(self) -> None:
        print(
            f"[Círculo] Raio: {self.raio:.2f} | Área: {self.calcular_area():.2f} | Perímetro: {self.calcular_perimetro():.2f} | Posição: {self.posicao}")


class Triangulo(Figura):
    """Especialização: Triângulo (definido por seus três lados e base/altura)."""

    def __init__(self, base: float, altura: float, lado_a: float, lado_b: float, lado_c: float, x: float = 0.0, y: float = 0.0, cor: str = "verde") -> None:
        super().__init__(x, y, cor_preenchimento=cor)
        self.base: float = base
        self.altura: float = altura
        self.lado_a: float = lado_a
        self.lado_b: float = lado_b
        self.lado_c: float = lado_c

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2.0

    def calcular_perimetro(self) -> float:
        return self.lado_a + self.lado_b + self.lado_c

    def descrever(self) -> None:
        print(f"[Triângulo] Base: {self.base:.2f}, Altura: {self.altura:.2f} | Área: {self.calcular_area():.2f} | Perímetro: {self.calcular_perimetro():.2f} | Posição: {self.posicao}")


class Retangulo(Figura):
    """Especialização: Retângulo (definido por largura e altura)."""

    def __init__(self, largura: float, altura: float, x: float = 0.0, y: float = 0.0, cor: str = "azul") -> None:
        super().__init__(x, y, cor_preenchimento=cor)
        if largura <= 0 or altura <= 0:
            raise ValueError("Largura e altura devem ser positivas.")
        self.largura: float = largura
        self.altura: float = altura

    def calcular_area(self) -> float:
        return self.largura * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.largura + self.altura)

    def descrever(self) -> None:
        print(f"[Retângulo] {self.largura:.2f}x{self.altura:.2f} | Área: {self.calcular_area():.2f} | Perímetro: {self.calcular_perimetro():.2f} | Posição: {self.posicao}")


class Quadrado(Retangulo):
    """
    Especialização do Retângulo: Quadrado.
    Herda de Retângulo, impondo que largura == altura == lado.
    """

    def __init__(self, lado: float, x: float = 0.0, y: float = 0.0, cor: str = "amarelo") -> None:
        super().__init__(largura=lado, altura=lado, x=x, y=y, cor=cor)
        self.lado: float = lado

    def descrever(self) -> None:
        print(
            f"[Quadrado] Lado: {self.lado:.2f} | Área: {self.calcular_area():.2f} | Perímetro: {self.calcular_perimetro():.2f} | Posição: {self.posicao}")


# ==============================================================================
# 3. HIERARQUIA DE FIGURAS TRIDIMENSIONAIS (ESPACIAIS)
# ==============================================================================

class Figura3D(Figura):
    """Subclasse abstrata para sólidos espaciais que possuem volume."""

    @abstractmethod
    def calcular_volume(self) -> float:
        pass


class Esfera(Figura3D):
    """Sólido geométrico espacial: Esfera."""

    def __init__(self, raio: float, x: float = 0.0, y: float = 0.0, cor: str = "ciano") -> None:
        super().__init__(x, y, cor_preenchimento=cor)
        self.raio: float = raio

    def calcular_area(self) -> float:
        """Área superficial da esfera (4 * pi * r^2)."""
        return 4 * math.pi * (self.raio ** 2)

    def calcular_perimetro(self) -> float:
        """Circunferência do equador da esfera."""
        return 2 * math.pi * self.raio

    def calcular_volume(self) -> float:
        """Volume da esfera ((4/3) * pi * r^3)."""
        return (4.0 / 3.0) * math.pi * (self.raio ** 3)

    def descrever(self) -> None:
        print(
            f"[Esfera 3D] Raio: {self.raio:.2f} | Área Superficial: {self.calcular_area():.2f} | Volume: {self.calcular_volume():.2f}")


# ==============================================================================
# Demonstração Prática de Polimorfismo
# ==============================================================================
if __name__ == "__main__":
    print("=== Demonstração da Hierarquia do Modelo Figura ===\n")

    # Lista polimórfica de diferentes figuras derivadas de Figura
    galeria_figuras: list[Figura] = [
        Circulo(raio=5.0, x=10.0, y=20.0, cor="Vermelho"),
        Retangulo(largura=8.0, altura=4.0, x=0.0, y=0.0, cor="Azul"),
        Quadrado(lado=6.0, x=5.0, y=5.0, cor="Amarelo"),
        Triangulo(base=10.0, altura=6.0, lado_a=10.0, lado_b=7.0,
                  lado_c=7.0, x=2.0, y=3.0, cor="Verde"),
        Esfera(raio=3.0, x=0.0, y=0.0, cor="Ciano")
    ]

    for fig in galeria_figuras:
        fig.descrever()

    print("\n--- Testando Movimentação Polimórfica ---")
    for fig in galeria_figuras[:3]:
        fig.mover(delta_x=2.5, delta_y=-1.0)
