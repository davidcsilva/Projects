'''
17.10 Crie uma classe base denominada Ponto que consta das coordenadas x e y. Dessa classe, derive uma classe
denominada Círculo que tenha um novo atributo denominado raio. Para essa classe derivada, os membros
dados x e y representam as coordenadas do centro de um círculo. Entre as funções membro da primeira classe,
deverá existir uma função distância() que devolva a distância entre dois pontos, onde
Distância = (x2 – x1) + (y2 – y1)



'''


import math


class Ponto:
    """Classe base que representa um ponto (x, y) no plano cartesiano."""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def distancia(self, outro: "Ponto", euclidiana: bool = True) -> float:
        """
        Calcula a distância entre este ponto e 'outro'.
        - euclidiana=True (padrão): sqrt((x2 - x1)^2 + (y2 - y1)^2)
        - euclidiana=False: expressão literal do enunciado (x2 - x1) + (y2 - y1)
        """
        if euclidiana:
            return math.hypot(outro.x - self.x, outro.y - self.y)
        return (outro.x - self.x) + (outro.y - self.y)

    def visualizar(self) -> str:
        return f"Ponto({self.x:g}, {self.y:g})"

    def __str__(self) -> str:
        return self.visualizar()


class Circulo(Ponto):
    """
    Classe derivada de Ponto:
    - Os atributos herdados (x, y) representam o centro do círculo.
    - Adiciona o atributo 'raio'.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0, raio: float = 1.0):
        super().__init__(x, y)
        if raio <= 0:
            raise ValueError("O raio do círculo deve ser maior que zero.")
        self.raio = float(raio)

    def area(self) -> float:
        return math.pi * (self.raio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.raio

    def contem_ponto(self, p: Ponto) -> bool:
        """Usa o método herdado distancia() para verificar se o ponto está dentro do círculo."""
        return self.distancia(p) <= self.raio

    def visualizar(self) -> str:
        return f"Círculo(Centro=({self.x:g}, {self.y:g}), Raio={self.raio:g})"

    def __str__(self) -> str:
        return self.visualizar()


# ==============================================================================
# EXEMPLO DE EXECUÇÃO
# ==============================================================================

if __name__ == "__main__":
    p1 = Ponto(1, 2)
    p2 = Ponto(4, 6)

    print("p1:", p1)
    print("p2:", p2)
    print(f"Distância euclidiana entre p1 e p2: {p1.distancia(p2):.2f}")
    print(
        f"Distância (fórmula literal do enunciado): {p1.distancia(p2, euclidiana=False):.2f}")

    print("-" * 55)

    c1 = Circulo(x=0, y=0, raio=5)
    c2 = Circulo(x=6, y=8, raio=3)

    print("c1:", c1)
    print(
        f"Área de c1: {c1.area():.2f} | Perímetro de c1: {c1.perimetro():.2f}")

    # Como Circulo herda de Ponto, distancia() funciona entre dois círculos (centros)
    # ou entre um círculo e um ponto
    print(f"Distância entre os centros de c1 e c2: {c1.distancia(c2):.2f}")
    print(f"O ponto {p2} está dentro de c1? {c1.contem_ponto(p2)}")
