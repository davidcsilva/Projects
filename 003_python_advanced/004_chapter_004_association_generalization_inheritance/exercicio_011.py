'''
17.11 Utilizando a classe construída no Exercício 17.10, obtenha uma classe derivada Cilindro derivada de Círcu-
lo. A classe Cilindro deverá ter uma função membro que calcule a superfície desse cilindro. A fórmula que
calcula a superfície do cilindro é S = 2r (l + r) onde r é o raio do cilindro e 1 é o comprimento.



'''


import math


class Ponto:
    """Nível 1: Classe base representando um ponto (x, y) no plano."""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def distancia(self, outro: "Ponto") -> float:
        return math.hypot(outro.x - self.x, outro.y - self.y)

    def visualizar(self) -> str:
        return f"Ponto({self.x:g}, {self.y:g})"

    def __str__(self) -> str:
        return self.visualizar()


class Circulo(Ponto):
    """Nível 2: Classe derivada de Ponto com centro (x, y) e raio."""

    def __init__(self, x: float = 0.0, y: float = 0.0, raio: float = 1.0):
        super().__init__(x, y)
        if raio <= 0:
            raise ValueError("O raio deve ser maior que zero.")
        self.raio = float(raio)

    def area(self) -> float:
        return math.pi * (self.raio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.raio

    def visualizar(self) -> str:
        return f"Círculo(Centro=({self.x:g}, {self.y:g}), Raio={self.raio:g})"


class Cilindro(Circulo):
    """
    Nível 3: Classe derivada de Círculo.
    - Herda (x, y) como coordenadas do centro da base e 'raio'.
    - Adiciona 'comprimento' (l).
    """

    def __init__(self, x: float = 0.0, y: float = 0.0, raio: float = 1.0, comprimento: float = 1.0):
        super().__init__(x, y, raio)
        if comprimento <= 0:
            raise ValueError(
                "O comprimento do cilindro deve ser maior que zero.")
        self.comprimento = float(comprimento)

    def superficie(self, incluir_pi: bool = True) -> float:
        """
        Calcula a área da superfície total do cilindro:
        - incluir_pi=True (padrão): S = 2 * pi * r * (l + r)
        - incluir_pi=False: fórmula literal do enunciado S = 2 * r * (l + r)
        """
        fator_pi = math.pi if incluir_pi else 1.0
        return 2 * fator_pi * self.raio * (self.comprimento + self.raio)

    def volume(self) -> float:
        """Calcula o volume reutilizando o método herdado area() da base circular."""
        return super().area() * self.comprimento

    def visualizar(self) -> str:
        return (
            f"Cilindro(Centro=({self.x:g}, {self.y:g}), "
            f"Raio={self.raio:g}, Comprimento={self.comprimento:g})"
        )


# ==============================================================================
# EXEMPLO DE EXECUÇÃO
# ==============================================================================

if __name__ == "__main__":
    cil1 = Cilindro(x=2, y=3, raio=4, comprimento=10)
    cil2 = Cilindro(x=5, y=7, raio=2, comprimento=6)

    print("cil1:", cil1)
    print(f"Área da base circular (herdada): {cil1.area():.2f}")
    print(f"Superfície total S = 2πr(l + r):  {cil1.superficie():.2f}")
    print(
        f"Superfície (literal S = 2r(l+r)): {cil1.superficie(incluir_pi=False):.2f}")
    print(f"Volume do cilindro:               {cil1.volume():.2f}")

    # Método distancia() herdado de Ponto (Nível 1) funciona diretamente entre cilindros
    print(
        f"Distância entre os centros de cil1 e cil2: {cil1.distancia(cil2):.2f}")
