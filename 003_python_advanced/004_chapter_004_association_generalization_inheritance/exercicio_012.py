'''
17.12 Crie uma classe base denominada Retângulo que contenha como membros dados, comprimento e largura.
Desta classe, derive uma classe denominada Caixa que tenha um membro adicional denominado profundidade
e outra função membro que permita calcular seu volume.


'''


class Retangulo:
    """Classe base representando um retângulo com comprimento e largura."""

    def __init__(self, comprimento: float = 1.0, largura: float = 1.0):
        if comprimento <= 0 or largura <= 0:
            raise ValueError(
                "Comprimento e largura devem ser maiores que zero.")
        self.comprimento = float(comprimento)
        self.largura = float(largura)

    def area(self) -> float:
        """Calcula a área do retângulo (comprimento × largura)."""
        return self.comprimento * self.largura

    def perimetro(self) -> float:
        """Calcula o perímetro do retângulo."""
        return 2 * (self.comprimento + self.largura)

    def visualizar(self) -> str:
        return f"Retângulo(Comprimento={self.comprimento:g}, Largura={self.largura:g})"

    def __str__(self) -> str:
        return self.visualizar()


class Caixa(Retangulo):
    """
    Classe derivada de Retângulo:
    - Herda 'comprimento' e 'largura' da base retangular.
    - Adiciona o membro 'profundidade' e o método volume().
    """

    def __init__(self, comprimento: float = 1.0, largura: float = 1.0, profundidade: float = 1.0):
        super().__init__(comprimento, largura)
        if profundidade <= 0:
            raise ValueError("A profundidade deve ser maior que zero.")
        self.profundidade = float(profundidade)

    def volume(self) -> float:
        """Calcula o volume da caixa reutilizando area() da classe base."""
        return super().area() * self.profundidade

    def area_superficie(self) -> float:
        """Calcula a área total das 6 faces da caixa."""
        return 2 * (
            self.comprimento * self.largura
            + self.comprimento * self.profundidade
            + self.largura * self.profundidade
        )

    def visualizar(self) -> str:
        return (
            f"Caixa(Comprimento={self.comprimento:g}, "
            f"Largura={self.largura:g}, Profundidade={self.profundidade:g})"
        )


# ==============================================================================
# EXEMPLO DE EXECUÇÃO
# ==============================================================================

if __name__ == "__main__":
    ret = Retangulo(comprimento=10, largura=5)
    print("Objeto base:", ret)
    print(f"Área do retângulo:      {ret.area():.2f}")
    print(f"Perímetro do retângulo: {ret.perimetro():.2f}")

    print("-" * 50)

    caixa = Caixa(comprimento=10, largura=5, profundidade=4)
    print("Objeto derivado:", caixa)
    print(f"Área da base (herdada): {caixa.area():.2f}")
    print(f"Volume da caixa:        {caixa.volume():.2f}")
    print(f"Área total da caixa:    {caixa.area_superficie():.2f}")
