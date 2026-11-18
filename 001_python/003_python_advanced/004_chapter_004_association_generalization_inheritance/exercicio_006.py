'''
17.6 Escreva uma classe FigGeométrica que representa figuras geométricas como ponto, linha, retângulo, tri-
ângulo e similares. Deve proporcionar métodos que permitam projetar, ampliar, mover e destruir tais objetos.
A hierarquia deve constar pelo menos de uma dezena de classes.


'''


import math
from abc import ABC, abstractmethod


# ==============================================================================
# NÍVEL 1: CLASSE BASE ABSTRATA
# ==============================================================================

class FigGeometrica(ABC):
    """Classe 1: Base para toda a hierarquia de figuras geométricas."""

    def __init__(self, nome: str):
        self.nome = nome
        self.ativa = True

    def _verificar_ativa(self) -> None:
        if not self.ativa:
            raise RuntimeError(
                f"Operação inválida: '{self.nome}' já foi destruída.")

    @abstractmethod
    def mover(self, dx: float, dy: float) -> None:
        """Desloca a figura em (dx, dy)."""

    @abstractmethod
    def ampliar(self, fator: float) -> None:
        """Amplia ou reduz a figura pelo fator especificado (> 0)."""

    @abstractmethod
    def projetar(self, eixo: str = "x") -> tuple:
        """Retorna a projeção ortogonal da figura sobre o eixo 'x' ou 'y'."""

    @abstractmethod
    def area(self) -> float:
        """Calcula a área da figura."""

    @abstractmethod
    def perimetro(self) -> float:
        """Calcula o perímetro (ou comprimento) da figura."""

    def destruir(self) -> str:
        """Marca o objeto como destruído e libera referências internas."""
        self._verificar_ativa()
        self.ativa = False
        return f"Objeto '{self.nome}' ({type(self).__name__}) destruído com sucesso."


# ==============================================================================
# NÍVEL 2: PONTO (0D), LINHA (1D) E FIGURA PLANA (2D)
# ==============================================================================

class Ponto(FigGeometrica):
    """Classe 2: Representa um ponto (x, y) no plano."""

    def __init__(self, x: float, y: float, nome: str = "Ponto"):
        super().__init__(nome)
        self.x = float(x)
        self.y = float(y)

    def mover(self, dx: float, dy: float) -> None:
        self._verificar_ativa()
        self.x += dx
        self.y += dy

    def ampliar(self, fator: float) -> None:
        self._verificar_ativa()
        if fator <= 0:
            raise ValueError("O fator de ampliação deve ser positivo.")
        # Um ponto tem dimensão zero; suas coordenadas permanecem inalteradas

    def projetar(self, eixo: str = "x") -> tuple[float, float]:
        self._verificar_ativa()
        eixo = eixo.lower()
        if eixo == "x":
            return (self.x, 0.0)
        elif eixo == "y":
            return (0.0, self.y)
        raise ValueError("Eixo inválido. Utilize 'x' ou 'y'.")

    def area(self) -> float:
        self._verificar_ativa()
        return 0.0

    def perimetro(self) -> float:
        self._verificar_ativa()
        return 0.0

    def __repr__(self) -> str:
        return f"({self.x:.2f}, {self.y:.2f})"


class Linha(FigGeometrica):
    """Classe 3: Segmento de reta entre dois pontos P1 e P2."""

    def __init__(self, p1: Ponto, p2: Ponto, nome: str = "Linha"):
        super().__init__(nome)
        self.p1 = p1
        self.p2 = p2

    def mover(self, dx: float, dy: float) -> None:
        self._verificar_ativa()
        self.p1.mover(dx, dy)
        self.p2.mover(dx, dy)

    def ampliar(self, fator: float) -> None:
        self._verificar_ativa()
        if fator <= 0:
            raise ValueError("O fator de ampliação deve ser positivo.")
        cx = (self.p1.x + self.p2.x) / 2.0
        cy = (self.p1.y + self.p2.y) / 2.0
        for p in (self.p1, self.p2):
            p.x = cx + (p.x - cx) * fator
            p.y = cy + (p.y - cy) * fator

    def projetar(self, eixo: str = "x") -> tuple[tuple[float, float], tuple[float, float]]:
        self._verificar_ativa()
        return (self.p1.projetar(eixo), self.p2.projetar(eixo))

    def area(self) -> float:
        self._verificar_ativa()
        return 0.0

    def perimetro(self) -> float:
        self._verificar_ativa()
        return math.hypot(self.p2.x - self.p1.x, self.p2.y - self.p1.y)

    def destruir(self) -> str:
        msg = super().destruir()
        self.p1 = None
        self.p2 = None
        return msg


class FiguraPlana(FigGeometrica, ABC):
    """Classe 4: Base abstrata para figuras bidimensionais com centro geométrico."""

    def __init__(self, centro: Ponto, nome: str):
        super().__init__(nome)
        self.centro = centro

    def mover(self, dx: float, dy: float) -> None:
        self._verificar_ativa()
        self.centro.mover(dx, dy)


# ==============================================================================
# NÍVEL 3, 4 e 5 (RAMO CURVO): CURVA FECHADA -> ELIPSE -> CÍRCULO
# ==============================================================================

class CurvaFechada(FiguraPlana, ABC):
    """Classe 5: Base abstrata para figuras planas de contorno curvo."""


class Elipse(CurvaFechada):
    """Classe 6: Elipse definida por centro, semieixo maior (a) e semieixo menor (b)."""

    def __init__(self, centro: Ponto, semieixo_a: float, semieixo_b: float, nome: str = "Elipse"):
        super().__init__(centro, nome)
        self.a = float(semieixo_a)
        self.b = float(semieixo_b)

    def ampliar(self, fator: float) -> None:
        self._verificar_ativa()
        if fator <= 0:
            raise ValueError("O fator de ampliação deve ser positivo.")
        self.a *= fator
        self.b *= fator

    def projetar(self, eixo: str = "x") -> tuple[tuple[float, float], tuple[float, float]]:
        self._verificar_ativa()
        eixo = eixo.lower()
        if eixo == "x":
            return ((self.centro.x - self.a, 0.0), (self.centro.x + self.a, 0.0))
        elif eixo == "y":
            return ((0.0, self.centro.y - self.b), (0.0, self.centro.y + self.b))
        raise ValueError("Eixo inválido. Utilize 'x' ou 'y'.")

    def area(self) -> float:
        self._verificar_ativa()
        return math.pi * self.a * self.b

    def perimetro(self) -> float:
        """Aproximação de Ramanujan para o perímetro da elipse."""
        self._verificar_ativa()
        h = ((self.a - self.b) ** 2) / ((self.a + self.b) ** 2)
        return math.pi * (self.a + self.b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))


class Circulo(Elipse):
    """Classe 7: Círculo (caso especial de Elipse onde a = b = raio)."""

    def __init__(self, centro: Ponto, raio: float, nome: str = "Círculo"):
        super().__init__(centro, raio, raio, nome)

    @property
    def raio(self) -> float:
        return self.a

    def perimetro(self) -> float:
        self._verificar_ativa()
        return 2 * math.pi * self.raio


# ==============================================================================
# NÍVEL 3, 4, 5 e 6 (RAMO POLIGONAL): POLÍGONO -> TRIÂNGULO / QUADRILÁTERO -> RETÂNGULO -> QUADRADO
# ==============================================================================

class Poligono(FiguraPlana, ABC):
    """Classe 8: Base abstrata para figuras delimitadas por segmentos de reta."""

    def __init__(self, vertices: list[Ponto], nome: str):
        cx = sum(p.x for p in vertices) / len(vertices)
        cy = sum(p.y for p in vertices) / len(vertices)
        super().__init__(Ponto(cx, cy), nome)
        self.vertices = vertices

    def mover(self, dx: float, dy: float) -> None:
        super().mover(dx, dy)
        for v in self.vertices:
            v.mover(dx, dy)

    def ampliar(self, fator: float) -> None:
        self._verificar_ativa()
        if fator <= 0:
            raise ValueError("O fator de ampliação deve ser positivo.")
        for v in self.vertices:
            v.x = self.centro.x + (v.x - self.centro.x) * fator
            v.y = self.centro.y + (v.y - self.centro.y) * fator

    def projetar(self, eixo: str = "x") -> tuple[tuple[float, float], tuple[float, float]]:
        self._verificar_ativa()
        eixo = eixo.lower()
        if eixo == "x":
            xs = [v.x for v in self.vertices]
            return ((min(xs), 0.0), (max(xs), 0.0))
        elif eixo == "y":
            ys = [v.y for v in self.vertices]
            return ((0.0, min(ys)), (0.0, max(ys)))
        raise ValueError("Eixo inválido. Utilize 'x' ou 'y'.")

    def perimetro(self) -> float:
        self._verificar_ativa()
        total = 0.0
        n = len(self.vertices)
        for i in range(n):
            p_atual = self.vertices[i]
            p_prox = self.vertices[(i + 1) % n]
            total += math.hypot(p_prox.x - p_atual.x, p_prox.y - p_atual.y)
        return total

    def area(self) -> float:
        """Calcula a área de qualquer polígono simples pela Fórmula de Shoelace."""
        self._verificar_ativa()
        n = len(self.vertices)
        soma = 0.0
        for i in range(n):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % n]
            soma += (p1.x * p2.y) - (p2.x * p1.y)
        return abs(soma) / 2.0

    def destruir(self) -> str:
        msg = super().destruir()
        self.vertices.clear()
        return msg


class Triangulo(Poligono):
    """Classe 9: Polígono de 3 vértices."""

    def __init__(self, p1: Ponto, p2: Ponto, p3: Ponto, nome: str = "Triângulo"):
        super().__init__([p1, p2, p3], nome)


class Quadrilatero(Poligono):
    """Classe 10: Polígono de 4 vértices."""

    def __init__(self, p1: Ponto, p2: Ponto, p3: Ponto, p4: Ponto, nome: str = "Quadrilátero"):
        super().__init__([p1, p2, p3, p4], nome)


class Retangulo(Quadrilatero):
    """Classe 11: Quadrilátero com ângulos retos definido por centro, largura e altura."""

    def __init__(self, centro: Ponto, largura: float, altura: float, nome: str = "Retângulo"):
        self.largura = float(largura)
        self.altura = float(altura)
        hw, hh = self.largura / 2.0, self.altura / 2.0
        vertices = [
            Ponto(centro.x - hw, centro.y - hh),
            Ponto(centro.x + hw, centro.y - hh),
            Ponto(centro.x + hw, centro.y + hh),
            Ponto(centro.x - hw, centro.y + hh),
        ]
        super().__init__(*vertices, nome=nome)

    def ampliar(self, fator: float) -> None:
        super().ampliar(fator)
        self.largura *= fator
        self.altura *= fator

    def area(self) -> float:
        self._verificar_ativa()
        return self.largura * self.altura


class Quadrado(Retangulo):
    """Classe 12: Caso especial de Retângulo com os quatro lados iguais."""

    def __init__(self, centro: Ponto, lado: float, nome: str = "Quadrado"):
        super().__init__(centro, lado, lado, nome)

    @property
    def lado(self) -> float:
        return self.largura


# ==============================================================================
# EXEMPLO DE EXECUÇÃO E DEMONSTRAÇÃO POLIMÓRFICA
# ==============================================================================

if __name__ == "__main__":
    figuras: list[FigGeometrica] = [
        Ponto(3, 4, "P1"),
        Linha(Ponto(0, 0), Ponto(6, 8), "Segmento AB"),
        Circulo(Ponto(5, 5), raio=3, nome="Círculo C1"),
        Elipse(Ponto(0, 0), semieixo_a=6, semieixo_b=3, nome="Elipse E1"),
        Triangulo(Ponto(0, 0), Ponto(4, 0), Ponto(
            0, 3), nome="Triângulo Retângulo"),
        Retangulo(Ponto(2, 2), largura=10, altura=4, nome="Retângulo R1"),
        Quadrado(Ponto(0, 0), lado=5, nome="Quadrado Q1"),
    ]

    print("=== ESTADO INICIAL DAS FIGURAS ===")
    for fig in figuras:
        print(
            f"{fig.nome:22s} | Área: {fig.area():7.2f} | "
            f"Perímetro: {fig.perimetro():7.2f} | Proj. X: {fig.projetar('x')}"
        )

    print("\n=== APLICANDO TRANSFORMAÇÕES NO QUADRADO Q1 ===")
    quad = figuras[-1]
    quad.mover(4, 2)       # Desloca o centro de (0, 0) para (4, 2)
    # Dobra o lado de 5 para 10 (área quadruplica de 25 para 100)
    quad.ampliar(2.0)
    print(
        f"Novo centro: {quad.centro} | Nova área: {quad.area():.2f} | Nova Proj. X: {quad.projetar('x')}")

    print("\n=== DESTRUINDO OBJETO ===")
    print(quad.destruir())
    try:
        quad.mover(1, 1)
    except RuntimeError as erro:
        print(f"Proteção verificada: {erro}")
